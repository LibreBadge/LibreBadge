from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "LibreBadge"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('login/', views.login_request, name='login'),
    url("logout/", views.logout_request, name="logout"),
    url(r'^production/(?P<slug>[-\w]+)/$', views.production, name="production"),
    url(r'^production/create/(?P<slug>[-\w]+)/$', views.productionCreate, name="production"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)