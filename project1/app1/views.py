from django.shortcuts import render
from  rest_framework import  viewsets
from  . serializers import  Student, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
