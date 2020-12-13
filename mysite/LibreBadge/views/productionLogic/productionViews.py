from ..imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
from django.http import Http404
import urllib.parse

@login_required
def production(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    return render(request, 'LibreBadge/production/production.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile})

@login_required
def productionCardholders(request, slug):
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
def productionRender(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    if request.method == 'POST':
        columns = list()
        values = list()
        received_json_data=(json.loads(request.body))[0]
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
def productionCreate(request, slug):
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
def productionUpdate(request, slug):
    try:
        BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
        BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
    except:
        raise Http404("Badge Template Doesn't Exist")
    if request.method == 'POST':
        columns = list()
        oldValues = list()
        newValues = list()
        received_json_data=json.loads(request.body)
        for i, JSONObj in enumerate(received_json_data):
            if not i:
                for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
                    postData = JSONObj.get(BadgeTemplateFormConfig['id'])
                    columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
                    oldValues.append(postData)
            else:
                for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
                    postData = JSONObj.get(BadgeTemplateFormConfig['id'])
                    newValues.append(postData)
        rows = formUpdate('cardholders', columns, 'cardholders', oldValues, newValues)
        return JsonResponse(rows, safe=False)
    else:
        raise Http404()

# old production create view, need to rework it to work with and like the other views
    @login_required
    def productionCreate(request, slug):
        try:
            BadgeTemplateInstance = BadgeTemplate.objects.get(slug=slug)
            BadgeTemplateConfigFile = json.loads(BadgeTemplateInstance.configFile.read())
        except:
            BadgeTemplateConfigFile = None
        if request.method == 'POST':
            columns = list()
            values = list()
            for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
                postData = request.POST.get(BadgeTemplateFormConfig['id'])
                columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
                values.append(postData)
            formCreate('cardholders', columns, 'cardholders', values)
            return render(request, 'LibreBadge/productionCreate.html',
            context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile,"createTab":"Active"})
        else:
            return render(request, 'LibreBadge/productionCreate.html',
            context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile, "createTab":"Active"})