from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import WelcomeMessage

# Create your views here.
@login_required
def index(request):
    return render(request, 'energized-id-django/home.html',
    context = {"WelcomeMessage":WelcomeMessage.objects.all})

@login_required
def logout_request(request):
    logout(request),
    messages.info(request, "Logged out syccessfully!"),
    return redirect("energized-id-django:index")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}!")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "energized-id-django/login.html",
                    context={"form":form})

@login_required
def cookietemplate(request):
    return render(request, 'energized-id-django/cookietemplate.html')