from django.shortcuts import render
from django.http import JsonResponse
from .models import student

# Create your views here.
def student_view(request):
    return render(request,"student/sview.html",{
        "students":student.objects.all(),
        "title":"Student View"
    })

#json api return all student recrods
def student_view2(request):
    student_record=student.objects.values().all()
    student_list=list(student_record)
    return JsonResponse({"data":student_list})