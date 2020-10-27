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
    url(r'^production/search/(?P<slug>[-\w]+)/$', views.productionSearch, name="productionSearch"),
    url(r'^production/create/(?P<slug>[-\w]+)/$', views.productionCreate, name="productionCreate"),
    url(r'^productionNEW/(?P<slug>[-\w]+)/$', views.productionNEW, name="productionNEW"),
    url(r'^productionNEW/(?P<slug>[-\w]+)/cardholders/$', views.productionNEWCardholders, name="productionNEWCardholders"),
    url(r'^productionNEW/(?P<slug>[-\w]+)/render/$', views.productionNEWrender, name="productionNEWrender"),
    url(r'^productionNEW/(?P<slug>[-\w]+)/update/$', views.productionNEWupdate, name="productionNEWupdate"),
    url('adminlte/', views.adminlte, name="adminlte"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)