# Generated by Django 5.0.6 on 2024-12-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_sifra_moeda_cifra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moeda',
            name='cifra',
        ),
        migrations.AddField(
            model_name='moeda',
            name='cifrao',
            field=models.CharField(max_length=50, null=True),
        ),
    ]