import numpy as np

def shell_sort(vetor):
    intervalo = len(vetor) // 2

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i

            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2

    return vetor


#Teste
print(shell_sort(np.array([15, 34, 8, 3])))

print(shell_sort(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])))
