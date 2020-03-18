from django.db import models
# Create your models here.

class BadgeTemplate(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    template = models.FileField(upload_to='badgeTemplates/',unique=True)
    def __str__(self):
        return self.name

class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.name