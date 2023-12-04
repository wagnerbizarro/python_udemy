import numpy as np

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio -1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        #Esquerda
        quick_sort(vetor, inicio, posicao - 1)
        #Direita
        quick_sort(vetor, posicao + 1, final)
    return vetor


#TESTE
vetor = np.array([15, 34, 8, 3])
print(quick_sort(vetor, 0, len(vetor) - 1))
