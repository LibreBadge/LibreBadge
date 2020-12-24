from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "LibreBadge"
applicationadminpatterns = [
    path('', views.applicationadmin, name='applicationadmin'),
    url(r'^alertmessages/update/(?P<pk>[-\w]+)/$', views.AlertMessageViews.get('UpdateView').as_view(), name='AlertMessageUpdate'),
    url(r'^alertmessages/create/', views.AlertMessageViews.get('CreateView').as_view(), name='AlertMessageCreate'),
    url('alertmessages/$', views.AlertMessageViews.get('ListView').as_view(), name='AlertMessageList'),
    url(r'^badgetemplates/update/(?P<pk>[-\w]+)/$', views.BadgeTemplateViews.get('UpdateView').as_view(), name='BadgeTemplateUpdate'),
    url(r'^badgetemplates/create/', views.BadgeTemplateViews.get('CreateView').as_view(), name='BadgeTemplateCreate'),
    url('badgetemplates/', views.BadgeTemplateViews.get('ListView').as_view(), name='BadgeTemplateList'),
]
urlpatterns = [
    path('', views.index, name='index'),
    url('login/', views.login_request, name='login'),
    url("logout/", views.logout_request, name="logout"),
    url(r'^production/(?P<slug>[-\w]+)/$', views.production, name="production"),
    url(r'^production/(?P<slug>[-\w]+)/cardholders/$', views.productionCardholders, name="productionCardholders"),
    url(r'^production/(?P<slug>[-\w]+)/render/$', views.productionRender, name="productionRender"),
    url(r'^production/(?P<slug>[-\w]+)/update/$', views.productionUpdate, name="productionUpdate"),
    path('applicationadmin/', include(applicationadminpatterns), name='applicationadmin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)