# Generated by Django 4.0.4 on 2022-05-17 06:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0028_alter_productdetails_available_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 11, 47, 21, 131083)),
        ),
    ]
