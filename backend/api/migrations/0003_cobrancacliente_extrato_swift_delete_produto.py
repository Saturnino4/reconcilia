# Generated by Django 5.0.6 on 2024-11-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_utilizador_role_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CobrancaCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_numero', models.CharField(max_length=60)),
                ('ope', models.CharField(max_length=60)),
                ('opr', models.CharField(max_length=60)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'Cobranças Cliente',
                'verbose_name_plural': 'Cobranças Clientes',
                'db_table': 'cobranca_cliente',
            },
        ),
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('documento', models.AutoField(primary_key=True, serialize=False)),
                ('data_mov', models.DateField()),
                ('data_ccb', models.DateField()),
                ('tipo_mov', models.CharField(max_length=60)),
                ('debito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'Extrato',
                'verbose_name_plural': 'Extratos',
                'db_table': 'extrato',
            },
        ),
        migrations.CreateModel(
            name='Swift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField()),
                ('code', models.CharField(max_length=60)),
                ('entr', models.CharField(max_length=60)),
                ('reference', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ma', models.CharField(choices=[('c', 'Crédito'), ('d', 'Débito')], max_length=1)),
                ('status', models.CharField(default='ativo', max_length=10)),
            ],
            options={
                'verbose_name': 'Swift',
                'verbose_name_plural': 'Swifts',
                'db_table': 'swift',
            },
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
