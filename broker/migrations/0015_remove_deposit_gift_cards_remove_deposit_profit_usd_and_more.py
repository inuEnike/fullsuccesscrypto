# Generated by Django 5.0.3 on 2024-03-20 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0014_wallet'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='gift_cards',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='profit_usd',
        ),
        migrations.AddField(
            model_name='deposit',
            name='plan',
            field=models.CharField(default='Silver', max_length=200),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('pin', models.CharField(default='0000', max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
