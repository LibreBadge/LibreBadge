from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    messages.success(request, 'Test message!'),
    return render(request, 'mywebapp/home.html')

def login(request):
    return render(request, 'mywebapp/login.html')

def logout_request(request):
    logout(request),
    messages.info(request, "Logged out syccessfully!"),
    return redirect("")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "mywebapp/login.html",
                    context={"form":form})