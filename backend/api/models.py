from django.db import models
from django.db.models import Sum


class Utilizador(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60)
    # role_id = models.ForeignKey('Role',related_name='role_id_U' ,on_delete=models.CASCADE, db_column='role_id',null=True)
    # role_name = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(default='ativo', max_length=10)
    class Meta:
        db_table = 'utilizador'
        verbose_name = 'Utilizador'
        verbose_name_plural = 'Utilizadores'
    def save(self, *args, **kwargs):
        if self.role_id:
            self.role_name = self.role_id.nome
        else:
            self.role_name = 'guest'
        super().save(*args, **kwargs)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, unique=True)

    status = models.CharField(default='ativo', max_length=10)
    class Meta:
        db_table = 'role'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class Permissao(models.Model):
    id = models.BigAutoField(primary_key=True)
    modulo = models.CharField(max_length=60)
    autorizacao = models.CharField(max_length=20)
    status = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'permissao'


class utilizador_role(models.Model):
    id = models.AutoField(primary_key=True)
    utilizador_id = models.ForeignKey('Utilizador',on_delete=models.CASCADE, related_name='utilizador_id_role', db_column='utilizador_id')
    role_id = models.ForeignKey('Role',on_delete=models.CASCADE, related_name='role_id_utili', db_column='role_id')
    status = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'utilizador_role'


class Role_permissao(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.ForeignKey('role',on_delete=models.CASCADE, related_name='role_id_permi', db_column='role_id')
    permissao_id = models.ForeignKey('Permissao',on_delete=models.CASCADE, related_name='permissao_id_utili', db_column='permissao_id')

    class Meta:
        db_table = 'role_permissao'



class Historico(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    acao = models.CharField(max_length=60)
    ip = models.CharField(max_length=60, null=True, blank=True)
    utilizador_id = models.ForeignKey('Utilizador', on_delete=models.CASCADE, related_name='utilizador_id_H' ,db_column='utilizador_id',null=True)
    status = models.CharField(default='ativo', max_length=10)
    class Meta:
        db_table = 'historico'
        verbose_name = 'Historico'
        verbose_name_plural = 'Historicos'

        


class tpcliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, unique=True)
    status = models.CharField(default='ativo', max_length=10)
    class Meta:
        db_table = 'tpcliente'
        verbose_name = 'Tipo de Cliente'
        verbose_name_plural = 'Tipos de Clientes'


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    foto = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=60, null=True, blank=True)
    endereco = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(default='ativo', max_length=10)
    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'



################################### Bussiness ########################################

class Extrato(models.Model):
    documento = models.AutoField(primary_key=True)
    data_mov = models.DateField()
    data_ccb = models.DateField()
    tipo_mov = models.CharField(max_length=60)
    debito = models.DecimalField(max_digits=10, decimal_places=2)
    credito = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'extrato'
        verbose_name = 'Extrato'
        verbose_name_plural = 'Extratos'


class Swift(models.Model):
    id          = models.AutoField(primary_key=True)
    value       = models.DecimalField(max_digits=10, decimal_places=2)
    data        = models.DateField()
    code        = models.CharField(max_length=60)
    entr        = models.CharField(max_length=60)
    reference   = models.TextField(null=True, blank=True)
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    ma          = models.CharField(max_length=1, choices=[('c', 'Crédito'), ('d', 'Débito')])
    status      = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table            = 'swift'
        verbose_name        = 'Swift'
        verbose_name_plural = 'Swifts'


class CobrancaCliente(models.Model):
    id = models.AutoField(primary_key=True)
    cli_numero = models.CharField(max_length=60)
    ope = models.CharField(max_length=60)
    opr = models.CharField(max_length=60)
    status = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'cobranca_cliente'
        verbose_name = 'Cobranças Cliente'
        verbose_name_plural = 'Cobranças Clientes'

        