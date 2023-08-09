# ----- Dicionarios ------

coleta = {"Aedes aegypt": 32, "Aedes Albopictus": 22, "Anopheles Darlingi": 14}

print(coleta["Aedes aegypt"])

print("\n")

# Adicionando
coleta["Rhodnius montenegrensis"] = 11
print(coleta)

print("\n")

# Apagando
# del(coleta) - tudo

# Um registro
del(coleta["Aedes aegypt"])
print(coleta)

print("\n")

# imprimir
print(coleta.items())

print("\n")

# imprimir somente as chaves
print(coleta.keys())

print("\n")

# Imprimir somente os valores
print(coleta.values())

print("\n")

# Merge de dicionarios
coleta2 = {"ABCDE": 13, "FGHI": 14}

coleta.update(coleta2)
print(coleta)

print("\n")

# Percorrer dicionario
for especie, num_especimes in coleta.items():
    print(f"Especie: {especie}, número coletados: {num_especimes}")
