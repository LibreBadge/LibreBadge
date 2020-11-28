from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:itemadmin"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:itemadmin"}
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
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == slug:
            AdminItem = item
    fields = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
    results = []
    for value in eval(AdminItem.get('model') + '.objects.values()'):
        fieldTypes2 = []
        for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
            fieldTypes2.append(field.get_internal_type())
        values2 = []
        for item in list(value.values()):
            values2.append(item)
        results.append(list(zip(values2, fieldTypes2)))
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/itemadmin.html',
    context = {"fields":fields, "results":results, "BadgeTemplate":BadgeTemplate.objects.all, "AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})