# Generated by Django 4.0.4 on 2022-05-10 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 13, 28, 50, 688623)),
        ),
    ]
