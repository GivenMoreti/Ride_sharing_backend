# Generated by Django 5.0.6 on 2024-06-29 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_rename_pickup_time_ride_pickup_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='rider',
        ),
    ]
