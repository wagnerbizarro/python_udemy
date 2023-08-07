# Ler 5 notas e informar a média
nota = media = soma = 0

for _ in range(1, 6):
    nota = float(input("Digite a nota:"))
    soma += nota

print(soma)

media = soma / 5
print('A media é:', media)

print("\n-------")

# Imprimir a tabuada do numero 3
i = 1
while i <= 10:
    print("3 x {} = {}".format(i, 3 * i))
    i += 1
