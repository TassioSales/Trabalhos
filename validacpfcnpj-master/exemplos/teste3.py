# Apenas alguns testes, por favor, ignore
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import validacpfcnpj

cpf_cnpj = validacpfcnpj.ValidaCpfCnpj()

arquivo = open("estagiario.txt", "r", enconding = "utf-8")
for item in arquivo:
    cpf_cnpj.cpf_cnpj = item
    if len(cpf_cnpj.cpf_cnpj) >= 14:
        if cpf_cnpj.valida():
            print(f'CNPJ {cpf_cnpj.cpf_cnpj} Válido.')
        else:
            print(f'CNPJ {cpf_cnpj.cpf_cnpj} Invalido.')
    if len(cpf_cnpj.cpf_cnpj) < 14:
        cpf_cnpj.cpf_cnpj = item
        if cpf_cnpj.valida():
            print(f'CPF {cpf_cnpj.cpf_cnpj} Válido.')
        else:
            print(f'CPF {cpf_cnpj.cpf_cnpj} Invalido.')

arquivo.close()


