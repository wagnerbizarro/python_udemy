# Conjuntos
biomoleculas = ("abc", "def", "ghy", "abc", "ghy", "ghy")

print(biomoleculas)

print("\n")

#somente os que não se repetem
print(set(biomoleculas))

print("\n")

# interseção
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}

c3 = c1.intersection(c2)

print(c3)

print("\n")

# Diferenca
c4 = c1.difference(c2)

print(c4)

