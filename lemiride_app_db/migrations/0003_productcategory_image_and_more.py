# Generated by Django 4.0.4 on 2022-05-11 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lemiride_app_db', '0002_productdetails_available_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.FileField(default='', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 8, 3, 11, 408689)),
        ),
    ]
