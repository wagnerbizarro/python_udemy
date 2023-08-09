idade = int(input("Digite sua idade:"))

if (idade < 0):
    print("Error: Número invalido")

else:
    if (idade <= 12):
        print("Criança")

    else:
        if (idade >= 13) & (idade <= 17):
            print("Adolescente")

        else:
            if (idade >= 18):
                print("Adulto")
