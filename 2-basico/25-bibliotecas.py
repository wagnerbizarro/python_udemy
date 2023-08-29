import math
r = math.sqrt(9) #raiz quadrada
print(r)
math.sin(45) #seno
math.cos(45) #coseno
math.log(32, 2) #logaritmo
math.e #constante euler
math.pi #constante pi


import datetime
d = dir(datetime) #Retorna todas as opções do datetime
print(d)


datetime.date.today() #data do dia
datetime.datetime.now() #hora atual

#definindo a data e informando
data = datetime.date(2020, 7, 10)
print(data)
print(data.day)
print(data.month)

#Definindo uma hora
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print(horario)
print(horario.hour)
print(horario.minute)
print(horario.second)
