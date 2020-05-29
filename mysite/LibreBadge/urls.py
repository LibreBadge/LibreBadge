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
    url(r'^production/test/(?P<slug>[-\w]+)/$', views.productionTest, name="productionTest"),
    url(r'^production/create/(?P<slug>[-\w]+)/$', views.productionCreate, name="productionCreate"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)