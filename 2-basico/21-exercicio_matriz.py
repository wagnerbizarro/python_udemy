#Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer
#e somar todos os elementos da matriz

import numpy as np

a = 0
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

print("\nMatriz: ", matriz)

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        a = matriz[i][j] + a

print("\nSoma dos valores: ", a)
