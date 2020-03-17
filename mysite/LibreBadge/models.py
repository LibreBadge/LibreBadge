from django.db import models
# Create your models here.

class BadgeTemplate(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    badge = models.FileField()
    def __str__(self):
        return self.name

class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.alert_name