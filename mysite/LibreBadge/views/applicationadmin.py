from django.contrib.auth import login
from .imports import *
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

AdminItems = [
    {"model":"BadgeTemplate", "title":"Badge Templates", "description":"Add or modify badge templates", "icon":"fas fa-id-badge", "url":"LibreBadge:BadgeTemplateList"},
    {"model":"AlertMessage", "title":"Alert Messages", "description":"Add or modify alert messages", "icon":"fas fa-exclamation-triangle", "url":"LibreBadge:AlertMessageList"}
]

@login_required
def applicationadmin(request):
    return render(request, 'LibreBadge/applicationadmin/home.html',
    context = {"AdminItems":AdminItems,})

class AlertMessageUpdate(LoginRequiredMixin, UpdateView):
    template_name = "LibreBadge/applicationadmin/AlertMessage/alertMessageForm.html"
    model = AlertMessage
    fields = "__all__"

class AlertMessageCreate(LoginRequiredMixin, CreateView):
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

class BadgeTemplateCreate(LoginRequiredMixin, CreateView):
    template_name = "LibreBadge/applicationadmin/BadgeTemplate/badgeTemplateList.html"
    model = BadgeTemplate

class BadgeTemplateList(LoginRequiredMixin, ListView):
    template_name = "LibreBadge/applicationadmin/BadgeTemplate/badgeTemplateList.html"
    model = BadgeTemplate

def applicationAdminCRUDFunction(model, modelName, fields):
    def templateNameGenerator(suffix):
        return("LibreBadge/applicationadmin/" + modelName + "/" + modelName + suffix + ".html")
    viewsDictionary = {}
    viewsDictionary['CreateView'] = type(modelName + 'CreateView', (CreateView,), {'template_name': templateNameGenerator('Form'),'model': model, 'fields': fields})
    viewsDictionary['ListView'] = type(modelName + 'ListView', (ListView,), {'template_name': templateNameGenerator('List'),'model': model})
    viewsDictionary['UpdateView'] = type(modelName + 'UpdateView', (UpdateView,), {'template_name': templateNameGenerator('Form'),'model': model, 'fields': fields})
    viewsDictionary['DeleteView'] = type(modelName + 'DeleteView', (CreateView,), {'success_url': reverse_lazy(modelName + 'Create'),'model': model})
    return(viewsDictionary)

AlertMessageViews = applicationAdminCRUDFunction(AlertMessage, 'AlertMessage', '__all__')
print(AlertMessageViews)

# class applicationAdminCRUD(object):
#     def __init__(self, model, fields):
#         class CreateView(LoginRequiredMixin, CreateView)
#         globals()[self.model.name][eval(self.model.name + 'Update')] = type(self.model.name + 'Update', (LoginRequiredMixin, UpdateView),{
#             'template_name':"LibreBadge/applicationadmin/" + self.model.name + "/" + self.model.name + "Form.html",
#             'model':self.model,
#             'fields':self.fields
#         })
#         globals()[self.model.name][eval(self.model.name + 'Create')] = type(self.model.name + 'Update', (LoginRequiredMixin, CreateView),{
#             'template_name':"LibreBadge/applicationadmin/" + self.model.name + "/" + self.model.name + "Form.html",
#             'model':self.model,
#             'fields':self.fields
#         })
#         globals()[self.model.name][eval(self.model.name + 'Create')] = type(self.model.name + 'Update', (LoginRequiredMixin, ListView),{
#             'template_name':"LibreBadge/applicationadmin/" + self.model.name + "/" + self.model.name + "List.html",
#             'model':self.model,
#         })

# BadgeTemplateViewsClass = applicationAdminCRUD(BadgeTemplate, "__all__")