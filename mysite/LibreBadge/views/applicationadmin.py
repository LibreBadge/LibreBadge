from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:modeladmin"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:modeladmin"}
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
def modeladmin(request,slug):
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == slug:
            AdminItem = item
    fields = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
    results = []
    for value in eval(AdminItem.get('model') + '.objects.values()'):
        fieldTypes = []
        for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
            fieldTypes.append(field.get_internal_type())
        values = []
        for item in list(value.values()):
            values.append(item)
        results.append(list(zip(values, fieldTypes)))
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/modeladmin.html',
    context = {"slug":slug, "fields":fields, "results":results, "BadgeTemplate":BadgeTemplate.objects.all, "AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})

@login_required
def itemadmin(request,modelslug,itemslug):
    AdminItem = {}
    for item in AdminItems:
        if item.get('model') == modelslug:
            AdminItem = item
    values = []
    for value in list(eval(AdminItem.get('model')+ ".objects.filter(pk=" + itemslug + ").values_list()"))[0]:
        values.append(value)
    fields = []
    fieldTypes = []
    for field in eval(AdminItem.get('model') + '._meta.get_fields()'):
        fields.append(field.name)
        fieldTypes.append(field.get_internal_type())
    results = zip(fields, fieldTypes, values)
    try:
        True
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/applicationadmin/itemadmin.html',
    context = {"results":results, "BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"title":AdminItem.get('title')})