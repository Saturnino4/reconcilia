# Generated by Django 5.0.6 on 2024-11-07 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilizador',
            name='role_id',
        ),
        migrations.RemoveField(
            model_name='utilizador',
            name='role_name',
        ),
    ]
