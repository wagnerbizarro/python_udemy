# Crie uma lista vazia e faça a leitura de dois valores do tipo float,
# colocando cada um dos valores nas primeiras posições da lista
# (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista)
# Faça a divisão dos dois valores e trate a seguinte exceções

# - ValuerError: se o usuário digitar um caracter
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# - IndexError: caso a divisão seja feita levando em consideração
# posições que não existem na lista
# - KeyboardInterrupt: caso o ousuário interrompa a execução

# Mostra uma mensagem personalizada na ocorrência de cada um desses erros

lista = []
try:
    lista.append(float(input("Digite o primeiro valor: ")))
    lista.append(float(input("Digite o segundo valor: ")))
    divisao = lista[0] / lista[1]
except ValueError:
    print("Erro! valor inválido")
except ZeroDivisionError:
    print("Erro! Divisão por zero")
except IndexError:
    print("Erro! Índice inválido")
except KeyboardInterrupt:
    print("Usuário interompeu a execução")
else:
    print(f"A divisão é {divisao}")