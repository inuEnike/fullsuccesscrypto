# Generated by Django 4.2.5 on 2023-09-11 13:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broker', '0009_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Customer',
        ),
    ]
