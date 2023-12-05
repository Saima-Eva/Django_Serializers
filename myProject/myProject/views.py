from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from myApp.models import*
from myApp.serializers import *


def myStudent(request,myid):

    student=Student_Model.objects.get(id=myid)
    Serializer_Data=Student_Serializer(student)


    json_data=JSONRenderer().render(Serializer_Data.data)

    return HttpResponse(json_data, content_type="application/json")


def myStudent_List(request):
    
    std=Student_Model.objects.all()

    Student_Serializer_Data=Student_Serializer(std, many=True)


    return JsonResponse(Student_Serializer_Data.data, safe=False)