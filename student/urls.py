from django.urls import path
from . import  views
urlpatterns=[
    path("",views.student_view,name="sview"),
    path("jsonview",views.student_view2,name="jsonview")
]