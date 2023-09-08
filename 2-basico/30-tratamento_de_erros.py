# Erro de sintaxe
#3 = 4

# Variavel nao definida
#print("Meu nome é", name)

#divisao por zero
#print(3 / 0)

#Erro de lista index
#c = [1,2,3,4,5]

#print c[5]


# Tratamento de erros
# try tentar executar o codigo
# except -excessão

#try:
#    n = int(input("Digite um numero inteiro: "))
#except:
#    print("Valor inválido")
#else:
#    print(f"Valor digitado é {n}")


#Loop ate que o valor correto seja informado

#while True:
# try:
#     n = int(input("Digite um numero inteiro: "))
# except:
#     print("Valor inválido")
# else:
#     print(f"Valor digitado é {n}")
#     break


#Tratamento com mensagem de acordo com o erro
while True:
    try:
        p = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido")
    except KeyboardInterrupt:
        print("Usuário interrompeu a execução")
        break
    else:
        print(f"Valor digitado é {p}")
        break
