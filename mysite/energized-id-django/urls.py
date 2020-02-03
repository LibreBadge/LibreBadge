from django.conf.urls import url
from django.urls import path

from . import views

app_name = "energized-id-django"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('login/', views.login_request, name='login'),
    url("logout/", views.logout_request, name="logout"),
]