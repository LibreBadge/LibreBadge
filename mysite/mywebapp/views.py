from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mywebapp/home.html')
# Create your views here.
