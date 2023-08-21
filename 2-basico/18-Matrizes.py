# Importando biblioteca para uso de matriz

import numpy as np

matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])

print ("Matriz:")
print (matriz)

print("\nEstrutura da Matriz: 2 linhas e 3 colunas ",matriz.shape)

print("\nA primeira linha: ",matriz[0])

print("\nA Segunda linha: ",matriz[1])

print("\nA Linha 0 e Coluna 0: ",matriz[0][0])

print("\nA Linha 1 e Coluna 1: ",matriz[0][0])

print("\n")
#Laço de repetição

for i in range(matriz.shape[0]):
    print(matriz[i])# percorrendo linha
    for j in range(matriz.shape[1]):
        print(matriz[i][j])# percorrendo coluna


