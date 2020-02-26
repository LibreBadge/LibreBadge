from .imports import *

# Create your views here.
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