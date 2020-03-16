from django.db import models
# Create your models here.

class BadgePage(models.Model):
    name = models.CharField(max_length=200)
    slug = models.TextField()
    badge = models.TextField()
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.badge_title

class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.alert_name