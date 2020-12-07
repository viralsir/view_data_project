from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="flight-home"),
    path("counter",views.showcounter,name="showcounter"),
    path("<int:flight_id>/",views.flight_det,name="flight_des"),
    path("book/<int:flight_id>",views.book,name="book")
]