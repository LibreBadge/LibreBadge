from .imports import *
import json
from .databaseFunctions import *
from .badgeTemplating import badgeTemplatingEngine
from django.http import JsonResponse
import urllib.parse

#Put all views that don't belong elsewere here
@login_required
def index(request):
    return render(request, 'LibreBadge/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all})

@login_required
def productionSearch(request, slug):
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
        return render(request, 'LibreBadge/productionSearch.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile,"rows":rows, "searchTab":"Active", "renderedBadgeTemplate":renderedBadgeTemplate})
    else:
        return render(request, 'LibreBadge/productionSearch.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile, "searchTab":"Active", "renderedBadgeTemplate":BadgeTemplateInstance.template})

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