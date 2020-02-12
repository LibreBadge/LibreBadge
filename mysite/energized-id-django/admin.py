from django.contrib import admin
from .models import WelcomeMessage
from .models import AlertMessage

# Register your models here.
admin.site.register(WelcomeMessage)
admin.site.register(AlertMessage)