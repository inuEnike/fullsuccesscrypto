# Generated by Django 5.0.6 on 2024-06-10 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0027_kyc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kyc',
            options={},
        ),
        migrations.RenameField(
            model_name='kyc',
            old_name='name',
            new_name='fname',
        ),
        migrations.AlterField(
            model_name='kyc',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
