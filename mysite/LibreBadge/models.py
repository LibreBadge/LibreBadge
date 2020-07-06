from django.db import models
# Create your models here.

class BadgeTemplate(models.Model):
    def upload_file_name(self, filename): #sets upload location
        return f'badgeTemplates/{self.name}/template/{filename}'
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True)
    template = models.FileField(upload_to=upload_file_name,unique=True)
    configFile = models.FileField(upload_to=upload_file_name,unique=True)
    def __str__(self):
        return self.name

class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.name