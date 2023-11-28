import numpy as np

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)
    

#Cabeça da lista
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro == None:
            print("A Lista está vazia")
            return None
        
        atual = self.primeiro
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo

    def pesquisa(self, valor):
        if self.primeiro == None:
            print("A Lista está vazia")
            return None
        
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                atual = atual.proximo
        return atual
    
    def excluir_inicio(self):
        if self.primeiro == None:
            print("A Lista está vazia")
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_posicao(self, valor):
        if self.primeiro == None:
            print("A Lista está vazia")
            return None
        
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual

#TESTE
lista = ListaEncadeada()

lista.insere_inicio(1)

lista.mostrar()

print(lista.primeiro)
## Mostra endereco de memória

lista.insere_inicio(2)
lista.mostrar()

print(lista.primeiro)
print(lista.primeiro.proximo)

lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)

lista.mostrar()

print(lista.primeiro)
print(lista.primeiro.proximo)
print(lista.primeiro.proximo.proximo)


###Excluir do inicio
lista.excluir_inicio()
lista.mostrar()


### Pesquisar
pesquisa = lista.pesquisa(3)

if pesquisa != None:
    print("Econtrado:" , pesquisa.valor)
else:
    print('Não encontrado')


### Excluir posicao
lista.excluir_posicao(3)
lista.mostrar()