#ex2

hora = input("Digite a hora atual: ")


try:

    hora = int(hora)

    if hora < 0 or hora > 23:

        print("Horario invalido! Digite um horario entre 0 e 23 horas")

    else:    

        if hora >= 0 and hora <= 11:

            print("Bom dia!")

        elif hora >= 12 and hora <=17:

            print("Boa tarde!")

        else:
            print("Boa noite! ")  

except ValueError:
    print("Horario invalido! Digite um horario interiro entre 0 e 23 horas")