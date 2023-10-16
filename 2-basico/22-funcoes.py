#Função privada, acessada somente pelo codigo não pelo usuário
#Precisa iniciar com __
def __pilha_cheia(self):
    print("abc")

#Função sem parametro
def mensagem():
    print("Texto da função")


mensagem()


# Função com parametro
def mensagem2(texto):
    print(texto)

mensagem2("Ola mundo!")


def soma(a, b):
    print(a + b)

soma(2, 3)


# Funcão com parametro e retorno

def soma2(a, b):
    return a + b

r = soma2(10, 20)
print(r)

# Função com parametro definido
def calcula_energia_potencial_gravitacional(m, h, g = 10):
    e = g * m * h
    return e

x = calcula_energia_potencial_gravitacional(30, 12)
print(x)

y = calcula_energia_potencial_gravitacional(30, 12, 9.8)
print(y)
