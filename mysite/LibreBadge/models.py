from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import shutil
from django.conf import settings
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

@receiver(pre_save, sender=BadgeTemplate) #deletes the old template when a new one is uploaded
def delete_old_template(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_template = BadgeTemplate.objects.get(pk=instance.pk)
        if instance.template and existing_template.template != instance.template:
            existing_template.template.delete(False)
    if instance.pk:
        existing_configFile = BadgeTemplate.objects.get(pk=instance.pk)
        if instance.configFile and existing_configFile.configFile != instance.configFile:
            existing_configFile.configFile.delete(False)

@receiver(pre_delete, sender=BadgeTemplate)
def delete_orphaned_template_files(sender, instance, *args, **kwargs):
    shutil.rmtree(settings.MEDIA_URL.replace("/","",1)+'badgeTemplates/'+instance.name+'/')

class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.name