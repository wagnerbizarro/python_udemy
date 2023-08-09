# ----- Tupla ------

tupla = ("Homo sapiens", "Canis Familiaris", "Felis Catus")

print(tupla)
print("\n")

print(tupla[0])

# Retorna a posicao
print(tupla.index("Canis Familiaris"))

# Percorrendo Tupla
for elemento in tupla:
    print(elemento)


# ---- Listas -----
l1 = ["Homo sapiens", "Canis Familiaris", "Felis Catus"]
l2 = ["Xenopus Laevis", "Ailuropoda Melanoleuca"]

l3 = l1 + l2

print(l3)

print("\n")

l2_2 = l2 * 2
print(l2_2)

print("\n")

# imprimi a partir do indice:x casas
print(l1[0:2])

# adicionando elementos
l1.append("Gorila gorila")
print(l1)

print("\n")

# Removendo elementos
l1.remove("Felis Catus")
print(l1)


print("\n")

# deletando lista
# del(l1)

# Percorrendo lista
for item in l2_2:
    print(item)
