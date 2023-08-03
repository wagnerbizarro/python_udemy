a = "casaco"

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

# Somente a primeira letra em maiusculo
capital = a.capitalize()
print(capital)

# Pegar metade da palavra
# Posicao index 0 ate 2
metade_palavra = a[0:3]
print(metade_palavra)


ultimas_letras = a[3:]
print(ultimas_letras)

# Substituir string
b =  a.replace("aco", "inha")
print(a)
print(b)

# Pesquisar na string

posicao = a.find("s")
print(posicao)

# Tamanho de variavel
e = " casaco "
print(len(e))

# Remover espaços em branco
f = e.strip()
print(f)

print(len(f))

# Mensagem formatada
n1 = 14
n2 = 16

print(f"Dividindo {n1} por {n2} o resultado é {n1/n2}")
