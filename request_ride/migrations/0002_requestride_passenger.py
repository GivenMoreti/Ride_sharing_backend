# Generated by Django 5.0.6 on 2024-06-29 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_ride', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestride',
            name='passenger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userprofile'),
        ),
    ]
