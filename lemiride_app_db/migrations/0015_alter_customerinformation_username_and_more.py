# Generated by Django 4.0.4 on 2022-05-15 11:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lemiride_app_db', '0014_remove_customerinformation_driving_license_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinformation',
            name='username',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='available_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 17, 18, 14, 868841)),
        ),
    ]