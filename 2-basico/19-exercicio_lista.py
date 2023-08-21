#Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
#e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
#para somar todos os valores digitados
l1 = []
i = 0
a = 0

while i < 5:
    number = int(input("Digite o número:"))
    i += 1
    print("Adicionando", number, "\n")
    l1.append(number)

print("\nLista: ", l1)

for iten in l1:
    a = iten + a

print("Soma dos valores: ", a)
