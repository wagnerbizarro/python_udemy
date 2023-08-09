m1 = float(input("Digite a note M1:"))
m2 = float(input("Digite a note M2:"))
m3 = float(input("Didigte a note M3:"))

media = (m1 + m2 + m3) / 3

mediaRound = round(media, 2)

print("\nNota:", mediaRound)

if (mediaRound <= 4.0):
    print("Reprovado")

else:
    if (mediaRound >= 4.1) & (mediaRound <= 6.0):
        print("Exame")

    else:
        if (mediaRound > 6.0):
            print("Aprovado")

