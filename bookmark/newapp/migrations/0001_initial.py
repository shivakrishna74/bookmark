# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newappdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=40)),
                ('apptype', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
    ]
