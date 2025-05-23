# Generated by Django 5.0.6 on 2024-06-29 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_remove_ride_rider'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='is_fully_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ride',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle'),
        ),
    ]
