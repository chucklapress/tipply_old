# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=50)),
                ('applicant_email', models.EmailField(max_length=30)),
                ('applicant_phone', models.IntegerField()),
                ('position_applying_for', models.CharField(max_length=80)),
                ('date_applying', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
