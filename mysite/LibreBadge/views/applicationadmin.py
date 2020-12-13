from django.contrib.auth import login
from .imports import *
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:BadgeTemplateList"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:AlertMessageList"}
]

@login_required
def applicationadmin(request):
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"BadgeTemplate":BadgeTemplate.objects.all,"AlertMessage":AlertMessage.objects.all, "AdminItems":AdminItems,})

class AlertMessageUpdate(LoginRequiredMixin, UpdateView):
    template_name = "LibreBadge/applicationadmin/AlertMessage/alertMessageForm.html"
    model = AlertMessage
    fields = "__all__"

class AlertMessageList(LoginRequiredMixin, ListView):
    template_name = "LibreBadge/applicationadmin/AlertMessage/alertMessageList.html"
    model = AlertMessage

class BadgeTemplateUpdate(LoginRequiredMixin, UpdateView):
    template_name = "LibreBadge/applicationadmin/BadgeTemplate/badgeTemplateForm.html"
    model = BadgeTemplate
    fields = "__all__"

class BadgeTemplateList(LoginRequiredMixin, ListView):
    template_name = "LibreBadge/applicationadmin/BadgeTemplate/badgeTemplateList.html"
    model = BadgeTemplate