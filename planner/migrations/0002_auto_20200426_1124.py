# Generated by Django 3.0.5 on 2020-04-26 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='meeting',
            name='start_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
