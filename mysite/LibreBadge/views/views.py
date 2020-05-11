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
        columns = []
        values = []
        for BadgeTemplateFormConfig in BadgeTemplateConfigFile['FormFields']:
            postDataVar = 'postData_' + BadgeTemplateFormConfig['id']
            exec(postDataVar + " = request.POST.get(BadgeTemplateFormConfig['id'])")
            columns.append(BadgeTemplateFormConfig['DatabaseColumn'])
            values.append('postData_' + BadgeTemplateFormConfig['id'])
        rows = formQuery('cardholders', columns, 'cardholders', values)
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile,"rows":rows})
    else:
        return render(request, 'LibreBadge/production.html',
        context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug,"BadgeTemplateConfigFile":BadgeTemplateConfigFile})

@login_required
def databaseTest(request):
    if request.method == 'POST':
        postid = request.POST.get("id")
        row = select("cardholders", "cardholders", "ID", postid)
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all, "row":row})
        row = "none"
    else:
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all})