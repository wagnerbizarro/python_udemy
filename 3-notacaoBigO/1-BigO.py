# Notação Big-O
# - Como comparar dois algoritmos?
# - Comparação objetiva entre algoritmos
# - Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
# - O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas
import timeit

# Função 1 O(n)
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += 1

    return soma

print("\nFunção1:")
print(timeit.timeit(lambda: soma1(10)))

# Função 2
def soma2(n):
    return(n *(n + 1) / 2
    )

print("\nFunção2:")
print(timeit.timeit(lambda: soma2(10)))

# Função 3
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista

l1 = lista1()
print("\nFunção3:")
print(timeit.timeit(lambda: l1))

# Função 4
def lista2():
    return range(1000)

l2 = lista2()
print("\nFunção4:")
print(timeit.timeit(lambda: l2))
