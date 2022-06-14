# Generated by Django 2.2.25 on 2022-05-06 09:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0002_eliot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ELIOT',
        ),
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac ', 'MAc - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines '), ('Switch ', 'Switch -To maintains and connect servers ')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 6, 9, 36, 14, 706402)),
        ),
    ]
