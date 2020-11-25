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
    url(r'^production/(?P<slug>[-\w]+)/cardholders/$', views.productionCardholders, name="productionCardholders"),
    url(r'^production/(?P<slug>[-\w]+)/render/$', views.productionRender, name="productionRender"),
    url(r'^production/(?P<slug>[-\w]+)/update/$', views.productionUpdate, name="productionUpdate"),
    url('applicationadmin/home', views.applicationadmin, name='applicationadmin'),
    url(r'^applicationadmin/(?P<slug>[-\w]+)/$', views.itemadmin, name='itemadmin'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)