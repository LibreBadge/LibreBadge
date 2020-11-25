from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

AdminItems = [
    {"model":"BadgeTemplates", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:itemadmin"},
    {"model":"AlertMessages", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:itemadmin"}
]

@login_required
def applicationadmin(request):
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all, "AdminItems":AdminItems, })

@login_required
def itemadmin(request,slug):
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/itemadmin.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"title":slug})