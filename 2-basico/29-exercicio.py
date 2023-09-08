# Crie um arquivo.py com duas funcoes
# - Função para ler uma string(recebe como parâmetro uma mensagem e retorna o
# que o usuário digitou)
#
# - Função para ler um número float(recebe como parâmetro uma mensageme retorna
# o que o usuário digitou)

import arquivo as ar

number = int(input("Digite sua idade:"))

name = str(input("Digite seu nome:"))

print(ar.number(number))
print(ar.string(name))
