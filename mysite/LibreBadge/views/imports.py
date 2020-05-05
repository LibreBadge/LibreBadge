#put all imports for views here
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..models import AlertMessage, BadgeTemplate