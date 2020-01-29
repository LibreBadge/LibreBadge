from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('login/', views.login, name='login'),
    url('flables/', views.flables, name='flables'),

]