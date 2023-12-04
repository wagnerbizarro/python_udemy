# Notavelmente lento e é o mais simples dos algoritmos de ordenação

# Funcionamento
# Comparação de dois números
# Se o da esquerda for maior, os elementos devem ser trocados
# Desloca-se uma posição á direita

# À medida que o algoritmo avança, os itens maiores "surgem como uma bolha" 
# na extremidade superior do vetor

import numpy as np

def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i - 1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    
    return vetor


#Teste
print(bubble_sort(np.array([15, 34, 8, 3])))