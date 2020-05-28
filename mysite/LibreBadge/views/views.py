from .imports import *
import json
#db test stuff
from .databaseFunctions import *
#Put all views that don't belong elsewere here
@login_required
def index(request):
    return render(request, 'LibreBadge/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all})

@login_required
def production(request, slug):
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
        rows = formQuery('cardholders', columns, 'cardholders', values)
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile,"rows":rows})
    else:
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile})

@login_required
def productionCreate(request,slug):
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
        rows = formCreate('cardholders', columns, 'cardholders', values)
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile,"rows":rows})
    else:
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile})
