from django.shortcuts import render
from django.http import HttpRequest
from utils.permissions import workit_staff

@workit_staff
def dashboard_view(request:HttpRequest):
    return render(request, 'layout/dashboard.html')