# Generated by Django 5.0.6 on 2024-12-05 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cobrancacliente_extrato_swift_delete_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
                'db_table': 'banco',
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('isnostra', models.IntegerField(default=0)),
                ('status', models.CharField(default='ativo', max_length=10)),
                ('banco_id', models.ForeignKey(db_column='banco_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conta_banco', to='api.banco')),
            ],
            options={
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
                'db_table': 'conta',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'local',
                'verbose_name_plural': 'locais',
                'db_table': 'local',
            },
        ),
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('sifra', models.CharField(max_length=50)),
                ('abreviatura', models.CharField(max_length=50)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'moeda',
                'verbose_name_plural': 'moedas',
                'db_table': 'moeda',
            },
        ),
        migrations.CreateModel(
            name='Nostro_vostro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'Nostro Vostro',
                'verbose_name_plural': 'Nostros Vostros',
                'db_table': 'nostro_vostro',
            },
        ),
        migrations.CreateModel(
            name='SubConta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'sub conta',
                'verbose_name_plural': 'sub contas',
                'db_table': 'subconta',
            },
        ),
        migrations.DeleteModel(
            name='CobrancaCliente',
        ),
        migrations.AddField(
            model_name='swift',
            name='conta_id',
            field=models.ForeignKey(db_column='conta_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='swift_conta', to='api.conta'),
        ),
        migrations.AddField(
            model_name='banco',
            name='local_id',
            field=models.ForeignKey(db_column='local_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banco_local', to='api.local'),
        ),
        migrations.AddField(
            model_name='conta',
            name='moeda_id',
            field=models.ForeignKey(db_column='moeda_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conta_moeda', to='api.moeda'),
        ),
        migrations.AddField(
            model_name='nostro_vostro',
            name='conta_id',
            field=models.ForeignKey(db_column='conta_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nostro_vostro_conta', to='api.conta'),
        ),
        migrations.AddField(
            model_name='subconta',
            name='conta_id',
            field=models.ForeignKey(db_column='conta_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subconta_conta', to='api.conta'),
        ),
        migrations.AddField(
            model_name='nostro_vostro',
            name='subconta_id',
            field=models.ForeignKey(db_column='subconta_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nostro_vostro_subconta', to='api.subconta'),
        ),
        migrations.AddField(
            model_name='extrato',
            name='subconta_id',
            field=models.ForeignKey(db_column='subconta_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcliente_subconta', to='api.subconta'),
        ),
    ]