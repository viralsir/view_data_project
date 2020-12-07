from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import flight,Pasenengers

# Create your views here.
def index(request):
    return render(request,"flights/index.html",{
        "flights":flight.objects.all()
    })

def showcounter(request):
    return render(request,"flights/counter.html")

def flight_det(request,flight_id):
    flight_details=flight.objects.get(pk=flight_id)

    return render(request,"flights/flight_details.html",{
        "flight":flight_details,
        "passengers":flight_details.passengers.all(),
        "non_passengers":Pasenengers.objects.exclude(flights=flight_details).all()
    })

def book(request,flight_id):
    if request.method == 'POST':
        flight_info=flight.objects.get(pk=flight_id)
        passenger_info=Pasenengers.objects.get(pk=int(request.POST["passenger_select"]))
        passenger_info.flights.add(flight_info)
        return HttpResponseRedirect(reverse("flight_des",args=(flight_id,)))

