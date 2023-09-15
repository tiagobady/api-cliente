import re
from validate_docbr import CPF

def validate_nome(nome):
    if nome.isalpha():
        return nome

def validate_cpf(numero_do_cpf):# Para criar uma função de validação, o nome deve ser validate
    cpf_validado = CPF()
    return cpf_validado.validate(numero_do_cpf)

def validate_rg(numero_do_rg):
    if len(numero_do_rg) == 9:
        return numero_do_rg
    
def validate_celular(numero_do_celular):
    """Verifica se o numero de celular é válido"""
    modelo = '[1-9]{2} [9][1-9]{4}-[0-9]{4}'
    resposta = re.findall(modelo, numero_do_celular)
    return resposta