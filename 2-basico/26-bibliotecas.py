import random
random.random() #Randomico

r = random.randint(1,5) #Randomico de 1 ate 5
print(r)

random.randrange(0, 10, 2) #Randmoico de 0 a 10 pulando de 2 em 2

x = ["K", "d", 13, "34-j"]

print(random.choice(x)) #Mostra valor aleatorio da lista

import time as tm #com apelido

tm.time() #Tempo atual em segundos

antes = tm.time()
lista = []
for i in range(0,10000):
    lista.append(i)
depois = tm.time()

print("Antes do for: ", antes)
print("Depois do for: ", depois)

intervalo = depois - antes

print(f"tempo: {intervalo} segundos")

print("Finalizando...")
tm.sleep(2)
print("...")
tm.sleep(2)
print("Concluído")
