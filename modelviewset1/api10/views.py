from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentROMVS(viewsets.ReadOnlyModelViewSetModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer