#Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
#fazendo a leitura dos valores por meio de uma estrutura de repetição.
#Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média

dic = {}
i = 0
x = 0
b = 0

while i < 3:
    name = str(input("Digite o nome: "))
    score = int(input("digite a nota: "))
    dic[name] = score
    i += 1

    #Calc
    b = dic[name] + b

print("Dicionario: ", dic)

result = b / 3
print("Media das notas: ", result)

