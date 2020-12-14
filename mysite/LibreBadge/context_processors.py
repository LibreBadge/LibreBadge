from .models import AlertMessage, BadgeTemplate

def GlobalContextVariables(request):
    return {
        "BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all
    }