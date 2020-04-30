from .imports import *
from django.db import connections
#Put all views that don't belong elsewere here
@login_required
def index(request):
    return render(request, 'LibreBadge/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all})

@login_required
def production(request, slug):
    return render(request, 'LibreBadge/production.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all,"slug":slug})

@login_required
def databaseTest(request):
    if request.method == 'POST':
        with connections['cardholders'].cursor() as cursor:
            cursor.execute("SELECT * FROM cardholders WHERE id = %s", [request.POST.get("id")])
            row = cursor.fetchall()
            cursor.close()
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all, "row":row})
        row = "none"
    else:
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all})