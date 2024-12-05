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
    subconta_id =      models.ForeignKey('SubConta', on_delete=models.CASCADE, related_name='subcliente_subconta' ,db_column='subconta_id',null=True)
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
    conta_id =    models.ForeignKey('Conta', on_delete=models.CASCADE, related_name='swift_conta' ,db_column='conta_id',null=True)
    status      = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table            = 'swift'
        verbose_name        = 'Swift'
        verbose_name_plural = 'Swifts'


class Banco(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    local_id = models.ForeignKey('Local', on_delete=models.CASCADE, related_name='banco_local' ,db_column='local_id',null=True)
    status = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'banco'
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'


class Local(models.Model):
    id          = models.AutoField(primary_key=True)
    pais        = models.CharField(max_length=50)
    cidade      = models.CharField(max_length=50)
    descricao   = models.CharField(max_length=50)
    status      = models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'local'
        verbose_name = 'local'
        verbose_name_plural = 'locais'



class Moeda(models.Model):
    id =            models.AutoField(primary_key=True)
    nome =          models.CharField(max_length=50)
    sifra =         models.CharField(max_length=50)
    abreviatura =   models.CharField(max_length=50)
    status =        models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'moeda'
        verbose_name = 'moeda'
        verbose_name_plural = 'moedas'


class Conta(models.Model):
    id =        models.AutoField(primary_key=True)
    nome =      models.CharField(max_length=50)
    banco_id =  models.ForeignKey('banco', on_delete=models.CASCADE, related_name='conta_banco' ,db_column='banco_id',null=True)
    moeda_id =  models.ForeignKey('moeda', on_delete=models.CASCADE, related_name='conta_moeda' ,db_column='moeda_id',null=True)
    isnostra =  models.IntegerField(default=0)
    status =    models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table = 'conta'
        verbose_name = 'conta'
        verbose_name_plural = 'contas'

class SubConta(models.Model):
    id =            models.AutoField(primary_key=True)
    nome =          models.CharField(max_length=50)
    conta_id =      models.ForeignKey('Conta', on_delete=models.CASCADE, related_name='subconta_conta' ,db_column='conta_id',null=True)
    status =        models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table =              'subconta'
        verbose_name =          'sub conta'
        verbose_name_plural =   'sub contas'

class Nostro_vostro(models.Model):
    subconta_id =   models.ForeignKey('SubConta', on_delete=models.CASCADE, related_name='nostro_vostro_subconta' ,db_column='subconta_id',null=True)
    conta_id =      models.ForeignKey('Conta', on_delete=models.CASCADE, related_name='nostro_vostro_conta' ,db_column='conta_id',null=True)
    status =        models.CharField(default='ativo', max_length=10)

    class Meta:
        db_table =              'nostro_vostro'
        verbose_name =          'Nostro Vostro'
        verbose_name_plural =   'Nostros Vostros'

# class extrato_subconta(models.Model):
#     subconta_id =   models.ForeignKey('SubConta', on_delete=models.CASCADE, related_name='extrato_subconta_subconta' ,db_column='subconta_id',null=True)
#     extrato_id =      models.ForeignKey('Extrato', on_delete=models.CASCADE, related_name='extrato_subconta_extrato' ,db_column='extrato_id',null=True)
#     status =        models.CharField(default='ativo', max_length=10)

#     class Meta:
#         db_table =              'extrato_subconta'
#         verbose_name =          'extrato subconta'
#         verbose_name_plural =   'extratos subcontas'

# class swift_conta(models.Model):
#     conta_id =      models.ForeignKey('Conta', on_delete=models.CASCADE, related_name='swift_conta_conta' ,db_column='conta_id',null=True)
#     swift_id =      models.ForeignKey('Swift', on_delete=models.CASCADE, related_name='swift_conta_swift' ,db_column='swift_id',null=True)
#     status =        models.CharField(default='ativo', max_length=10)

#     class Meta:
#         db_table =              'swift_conta'
#         verbose_name =          'swift conta'
#         verbose_name_plural =   'swifts contas'






        