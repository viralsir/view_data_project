from django.test import TestCase,Client
from .models import airport,flight
#      100
#      200
#      300
#      400
#      500
# Create your tests here.
class FlightTest(TestCase):

    def setUp(self) :

        # create airport objects
        a1 = airport.objects.create(code="ahm",city="Ahmedabad")
        a2 = airport.objects.create(code="bor", city="Baroda")
        a3 = airport.objects.create(code="sur", city="Surat")

        # create a flight objects
        f1=flight.objects.create(origin=a1,destion=a2,duration=200)
        f2=flight.objects.create(origin=a1,destion=a3,duration=300)
        f3=flight.objects.create(origin=a1,destion=a1,duration=-150)


    def test_departure_count(self):
        a=airport.objects.get(code="ahm")
        self.assertEqual(a.departure.count(),3)


    def test_arrival_count(self):
        a=airport.objects.get(code="sur")
        self.assertEqual(a.arrivals.count(),1)

    def test_valid_flight(self):
        a1=airport.objects.get(code="ahm")
        a3=airport.objects.get(code="sur")
        fl=flight.objects.get(origin=a1,destion=a3)
        self.assertTrue(fl.is_valid_flight())

    def test_valid_flight_duration(self):
        fl = flight.objects.get(duration=300)
        self.assertTrue(fl.is_valid_flight())

    def test_invalid_flight(self):
        a1=airport.objects.get(code="ahm")
        fl=flight.objects.get(origin=a1,destion=a1)
        self.assertFalse(fl.is_valid_flight())

    def test_invalid_duration(self):
        fl=flight.objects.get(duration=-150)
        self.assertFalse(fl.is_valid_flight())

    def test_index(self):
        c=Client()
        response=c.get("/flights/")
        self.assertEqual(response.status_code,200)

    def test_index_context(self):
        c=Client()
        response=c.get("/flights/")
        self.assertEqual(response.context["flights"].count(),2)
