import random

while True:
    print("             MENU                ")
    print("__________________________________")
    print("1 - Gerar CPF")
    print("2 - Validar CPF")
    print("3 - Sair")
    try:
        opcao = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao == 1:
        cpf = []
        for i in range(9):
            cpf.append(random.randint(0,9))

        soma = 0
        for i in range(9):
            digito = int(cpf[i])
            peso = 10 - i
            soma += digito * peso
            
        resto = soma % 11    
        if resto < 2:
            primeiro_digito = 0
        elif resto >= 2:
            primeiro_digito = 11 - resto  

        cpf.append(primeiro_digito)

        soma2 = 0
        for i in range(10):
            digito = int(cpf[i])
            peso = 11 - i
            soma2 += digito * peso

        resto2 = soma2 % 11
        if resto2 < 2:
            segundo_digito = 0
        elif resto2 >= 2:
            segundo_digito = 11 - resto2  
        
        cpf.append(segundo_digito)  
        cpf_formatado = f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
        print(f"CPF gerado: {cpf_formatado}")
        
    
    elif opcao == 2:
        while True:
            cpf = input("Digite seu cpf: ")

            cpf_formatado = cpf.replace(".", "").replace("-", "").strip()

            if cpf_formatado.isdigit() and len(cpf_formatado) == 11:

                cpf_lista = list(cpf_formatado)
                break
            else:
                print("CPF inválido, tente novamente")

        soma = 0
        for i in range(9):
            digito = int(cpf_lista[i])
            peso = 10 - i
            soma += digito * peso
            
        resto = soma % 11    
        if resto < 2:
            primeiro_digito = 0
        elif resto >= 2:
            primeiro_digito = 11 - resto  

        soma2 = 0
        for i in range(10):
            digito = int(cpf_lista[i])
            peso = 11 - i
            soma2 += digito * peso

        resto2 = soma2 % 11
        if resto2 < 2:
            segundo_digito = 0
        elif resto2 >= 2:
            segundo_digito = 11 - resto2  

        if int(cpf_lista[9]) == primeiro_digito and int(cpf_lista[10]) == segundo_digito:
            print(f"\nO CPF digitado '{cpf}' é valido!!")
        else:
            print(f"\nO CPF digitado '{cpf} é invalido, tente novamente'")    

    elif opcao == 3:
    
        print("Saindo...")
        exit(0)
    
    else:
        print("A opção digitada não existe, tente novamente")
