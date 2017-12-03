# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0008_auto_20171202_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='birthdayVisible',
            field=models.BooleanField(default=False, help_text='Make birthday visible to others'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='existingEmail',
            field=models.EmailField(blank=True, help_text='Existing <em>@jacobs-alumni.de</em> email address (if you have one)', max_length=254, null=True),
        )
    ]
