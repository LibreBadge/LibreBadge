# Generated by Django 3.0.2 on 2020-02-12 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibreBadge', '0003_alertmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertmessage',
            name='alert_expires',
        ),
        migrations.RemoveField(
            model_name='alertmessage',
            name='alert_expiresDate',
        ),
    ]
