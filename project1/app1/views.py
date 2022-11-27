from ast import Is
from django.shortcuts import render
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


# Create your views here.
class EmployeeDetails(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    