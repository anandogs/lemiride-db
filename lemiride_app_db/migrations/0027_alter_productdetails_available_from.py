# Generated by Django 4.0.4 on 2022-05-16 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0026_alter_productdetails_available_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 19, 41, 56, 69447)),
        ),
    ]
