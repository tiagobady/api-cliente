from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *



class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "O Numero de CPF não é válido!"})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({"nome": "Não inclua números neste campo!"})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({"rg": "RG deve conter 9 dígitos"})
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({"celular": "Insira o numero de celular no modelo DD 9XXXX-XXXX"})
        return data
    
    

    
