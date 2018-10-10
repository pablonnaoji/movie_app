# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-10 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=4)),
                ('plot', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField()),
            ],
        ),
    ]
