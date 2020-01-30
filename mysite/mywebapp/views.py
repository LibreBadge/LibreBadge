from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'mywebapp/home.html')

def login(request):
    return render(request, 'mywebapp/login.html')

def register(request):
    form = UserCreationForm
    return render(request, 
                   "mywebapp/register.html",
                   context={"form":form} )

def logout_request(request):
    logout(request),
    messages.info(request, "Logged out syccessfully!"),
    return redirect("")

def login_request(request):
    form = AuthenticationForm(),
    return render(request,
                    "mywebapp/login.html",
                    context={"form":form} )