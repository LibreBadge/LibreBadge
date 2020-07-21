from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
import urllib.parse

@login_required
def productionNEW(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
       BadgeTemplateConfigFile = None
       BadgeTemplateInstance = None
    if request.method == 'POST':
        columns = list()
        values = list()
        for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
            postData = request.POST.get(BadgeTemplateFormConfig['id'])
            columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
            values.append(postData)
        rows = formQuery('cardholders', columns, 'cardholders', values)
        renderedBadgeTemplate = badgeTemplatingEngine(BadgeTemplate.objects.get(slug=slug), rows)
        return render(request, 'LibreBadge/productionNEW.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile, "renderedBadgeTemplate":renderedBadgeTemplate})
    else:
        return render(request, 'LibreBadge/productionNEW.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile, "renderedBadgeTemplate":BadgeTemplateInstance.template})

@login_required
def productionNEWCardholders(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
       BadgeTemplateConfigFile = None
       BadgeTemplateInstance = None
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
       BadgeTemplateConfigFile = None
       BadgeTemplateInstance = None
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
       BadgeTemplateConfigFile = None
       BadgeTemplateInstance = None
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