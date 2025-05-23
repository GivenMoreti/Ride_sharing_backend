# Generated by Django 5.0.6 on 2024-06-29 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ride', '0003_remove_ride_rider'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
                ('time_edited', models.DateTimeField(auto_now=True)),
                ('cancel_request', models.BooleanField(default=False)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride.ride')),
            ],
        ),
    ]
