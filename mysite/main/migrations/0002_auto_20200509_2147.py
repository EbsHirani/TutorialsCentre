# Generated by Django 3.0.6 on 2020-05-09 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 9, 21, 47, 31, 683439), verbose_name='date published'),
        ),
    ]
