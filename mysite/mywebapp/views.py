from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mywebapp/home.html')

def login(request):
    return render(request, 'mywebapp/login.html')

def flables(request):
    return render(request, 'mywebapp/floating-labels.html')