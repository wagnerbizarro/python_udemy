# Ler uma temperatura em graus Celsius e
# apresentá-la convertida em graus Fahrenheit.
# A fórmula de conversão é F = (9 * C + 160)/5,
# na qual F é a temperatura em Fahrenheit e C é a temperatura
# em graus Celsius
#
# - Função para ler e retornar o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo(recebe o parâmetro em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor
# e fazendo a impressão

def ler_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def converter(temperatura_celsius):
    temperatura_f = (9 * temperatura_celsius + 160) / 5
    return temperatura_f

def mostrar(temperatura_f):
    print(temperatura_f)

temperatura_c = ler_temperatura()
temperatura_f = converter(temperatura_c)
mostrar(temperatura_f)
