class Triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        #Atributos
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura

        #Metodos
    def area(self):
        return (self.base * self.altura) / 2
    
    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return "não é um triângulo"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
            return "Triângulo isósceles"
        else:
            return "Outro tipo de triângulo"

t1 = Triangulo(5, 1, 3, 4, 5)
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)
print(t1.area())
print(t1.tipo())

t2 = Triangulo(6, 2, 4, 7, 8)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)
print(t2.area())
print(t2.tipo())