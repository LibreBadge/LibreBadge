from django.contrib import admin
from .models import BadgePage
from .models import AlertMessage

# Register your models here.
admin.site.register(BadgePage)
admin.site.register(AlertMessage)