from django.contrib import admin
from .models import AlertMessage, BadgeTemplate

# Register your models here.
admin.site.register(BadgeTemplate)
admin.site.register(AlertMessage)