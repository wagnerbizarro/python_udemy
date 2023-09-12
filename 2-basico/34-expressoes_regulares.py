# Metodos 
# search: encontrar padrões dentro de uma string
# match: verificar se é igual
# findall: encontrar todas as substrings

# Metacaracteres
# . - Qualquer caractere(excente linha nova)
# \w - Qualquer caractere alfanumérico
# \W - Qualquer caractere não-alfanumérico
# \d - Qualquer caractere que seja um dígito(0-9)
# \D - Qualquer caractere não dígito
# \s - Espaço em branco
# ^ - começa com 
# $ - termina com 
# "\" - usado antes de metacaracteres para especificar seu significado literal


# Quantificadores
# [] - Opcional entre os que estão dentro dos colchetes
# () - captura grupos de caracteres
# * - de zero a mais vezes
# ? - zero ou uma vez
# + - uma ou mais vezes
# {m,n} - de m a n vezes
# | - ou



# exemplos
import re
frase1 = 'Olá, meu número de telefone é (42)0000-0000'

frase2 = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'

frase3 = 'Entre em contato, meu email é teste@teste.com'

#SEARCH
telefone = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase1)
print(telefone)


placa = re.search('[A-Za-z]{3}-\d{4}', frase2) 
print(placa)

email = re.search('\w+@\w+\.com', frase3)
print(email)

#MATCH
print(re.match('[A-Za-z]{3}-\d{4}', frase2)) 


#Findall
frase4 = "Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo"

print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase4))


emails = '''
Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

print(re.findall('\w+@\w+\.\w*', emails))