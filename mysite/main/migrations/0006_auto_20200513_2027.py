# Generated by Django 3.0.6 on 2020-05-13 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200513_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 20, 27, 34, 382933), verbose_name='date published'),
        ),
    ]
