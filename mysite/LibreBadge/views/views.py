from .imports import *
#db test stuff
from django.db import connections
from collections import namedtuple
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

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
        postid = request.POST.get("id")
        with connections['cardholders'].cursor() as cursor:
            cursor.execute("SELECT * FROM %s WHERE ID = %s",['cardholders',postid])
            row = namedtuplefetchall(cursor)
            cursor.close()
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all, "row":row})
        row = "none"
    else:
        return render(request, 'LibreBadge/databaseTest.html',
        context = {"AlertMessage":AlertMessage.objects.all})