# Generated by Django 3.0.8 on 2020-07-27 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp_1', '0002_auto_20200727_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 12, 37, 41, 810789, tzinfo=utc)),
        ),
    ]
