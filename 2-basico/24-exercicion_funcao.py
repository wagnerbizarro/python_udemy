# Efetuar o cálculo da quantidade de litros de combustível gasto em
# uma viagem, utlizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto
# na viagem e a velocidade média durante ela. Desta forma, será
# possível obter a distância percorrida com a fórmula
# DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta
# calcular a quantidade de litros de combustível utilizada na viagem,
# com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve
# apresentar os valores da velocidade média, tempo gasto na viagem,
# a distância percorrida e a quantidade de litros utilizada na
# viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a
# velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a
# distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e
# somente imprime o resultado)

def leitura():
    tempo =  float(input("Digite o tempo da viagem: "))
    velocidade = float(input("Digite a velocidade média: "))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia / 12

def imprime(velocidade, tempo, distancia, litros):
    print("Velocidade:", velocidade)
    print("Tempo:", tempo)
    print("Distância:", distancia)
    print("Litros:", litros)


t, v = leitura()
d = calcula_distancia(t, v)
l = calcula_litros(d)
imprime(v, t, d, l)
