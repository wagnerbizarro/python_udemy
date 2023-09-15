class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0
    
    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra_dados(self):
        print("Nome: ", self.nome)
        print("Nota 1: ", self.nota1)
        print("Nota 2: ", self.nota2)
        print("Média: ", self.media)

    def resultado(self):
        if self.media >= 6.0:
            print("Aprovado")
        else:
            print("Reprovado")


aluno1 = Aluno("João", 7.0, 2.0)
aluno1.calcula_media()
aluno1.mostra_dados()
aluno1.resultado()