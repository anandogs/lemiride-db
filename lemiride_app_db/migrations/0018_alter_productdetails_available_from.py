# Generated by Django 4.0.4 on 2022-05-15 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0017_alter_productdetails_available_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 17, 29, 39, 419546)),
        ),
    ]
