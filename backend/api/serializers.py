from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

class SwiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swift
        fields = '__all__'

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = '__all__'

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'

class UtilizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilizador
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

