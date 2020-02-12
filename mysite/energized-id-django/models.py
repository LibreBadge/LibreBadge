from django.db import models
# Create your models here.

class WelcomeMessage(models.Model):
    welcome_title = models.CharField(max_length=200)
    welcome_content = models.TextField()
    welcome_published = models.DateTimeField('date published')

    def __str__(self):
        return self.welcome_title

class AlertMessage(models.Model):
    alert_name = models.CharField(max_length=200)
    alert_color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    alert_content = models.TextField()
    alert_dismissable = models.BooleanField()

    def __str__(self):
        return self.alert_name