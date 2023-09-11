with open('/home/wagner/Projetos/python_udemy/2-basico/frase1.txt') as text:
    #for linha in text:
    #    print(linha)

    
    #Salvando o conteudo do arquivo em uma lista
    r = text.readlines()
    #print(r)

    #Criando um novo arquivo
with open("/home/wagner/Projetos/python_udemy/2-basico/texto.txt", "w") as texto:
    texto.write("Olá a todos")

    #Lendo o novo arquivo
with open("/home/wagner/Projetos/python_udemy/2-basico/texto.txt", "r") as textt:
    for linha in textt:
        print(linha)
