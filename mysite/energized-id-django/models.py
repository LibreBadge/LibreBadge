from django.db import models
# Create your models here.

class WelcomeMessage(models.Model):
    welcome_title = models.CharField(max_length=200)
    welcome_content = models.TextField()
    welcome_published = models.DateTimeField('date published')

    def __str__(self):
        return self.welcome_title