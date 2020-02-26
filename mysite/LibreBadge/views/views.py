from .imports import *
#Put all views that don't belong elsewere here
@login_required
def index(request):
    return render(request, 'LibreBadge/home.html',
    context = {"WelcomeMessage":WelcomeMessage.objects.all,"AlertMessage":AlertMessage.objects.all})

@login_required
def cookietemplate(request):
    return render(request, 'LibreBadge/cookietemplate.html',
    context = {"AlertMessage":AlertMessage.objects.all})

@login_required
def databaseTest(request):
    return render(request, 'LibreBadge/databaseTest.html',
    context = {"AlertMessage":AlertMessage.objects.all})