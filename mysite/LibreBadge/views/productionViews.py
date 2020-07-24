from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

@login_required
def productionNEW(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/productionNEW.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile})

@login_required
def productionNEWCardholders(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    columns = list()
    for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
        columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
    rows = query('cardholders', columns, 'cardholders')
    return JsonResponse(rows, safe=False)

@login_required
def productionNEWrender(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    if request.method == 'POST':
        columns = list()
        values = list()
        received_json_data=json.loads(request.body)
        for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
            postData = received_json_data.get(BadgeTemplateFormConfig['id'])
            columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
            values.append(postData)
        rows = formQuery('cardholders', columns, 'cardholders', values)
        renderedBadgeTemplate = badgeTemplatingEngine(BadgeTemplate.objects.get(slug=slug), rows)
        return HttpResponse(renderedBadgeTemplate)
    else:
        return HttpResponse(BadgeTemplateInstance.template)

@login_required
def productionNEWcreate(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    if request.method == 'POST':
        columns = list()
        values = list()
        received_json_data=json.loads(request.body)
        for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
            postData = received_json_data.get(BadgeTemplateFormConfig['id'])
            columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
            values.append(postData)
        rows = formCreate('cardholders', columns, 'cardholders', values)
        renderedBadgeTemplate = badgeTemplatingEngine(BadgeTemplate.objects.get(slug=slug), rows)
        return HttpResponse(renderedBadgeTemplate)
    else:
        return HttpResponse(BadgeTemplateInstance.template)

@login_required
def productionNEWupdate(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    if request.method == 'POST':
        columns = list()
        values = list()
        received_json_data=json.loads(request.body)
        for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
            postData = received_json_data.get(BadgeTemplateFormConfig['id'])
            columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
            values.append(postData)
        rows = formUpdate('cardholders', columns, 'cardholders', values)
        renderedBadgeTemplate = badgeTemplatingEngine(BadgeTemplate.objects.get(slug=slug), rows)
        return JsonResponse(rows, safe=False)