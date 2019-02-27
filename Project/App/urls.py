from django.shortcuts import render
# from django.http import HttpResponse
# from . forms import EmployeeApplication
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ApplicationForm/', views.index, name="ApplicationForm"),
    path('gotEmployeeInfo/', views.index, name="gotEmployeeInfo"),
    path('newForm/', views.index, name="adoption"),
    ]