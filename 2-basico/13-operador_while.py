# Basico

# Incremento
numero = 1
while numero < 6:
    print(numero)
    numero += 1
print("---\n")

# Decremento
numero = 5
while numero > 0:
    print(numero)
    numero -= 1
print("---\n")

# Soma
soma = 0
numero = 1
while numero < 6:
    soma += numero
    numero += 1
    print(soma)
print("---\n")

# Só sai do loop com a validação do valor
numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Digite um número de 1 a 10: "))
print("---\n")
