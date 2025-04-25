sair = ''
while sair != "S":
    while True:
        num1 = input("Digite o primeiro operador da sua conta: ")

        try:
            num1 = float(num1)
            break
        except ValueError:
            print("Você não digitou um número válido. Tente novamente.")

    while True:
        num2 = input("Digite o segundo operador da sua conta: ")

        try:
            num2 = float(num2)
            break
        except ValueError:
            print("Você não digitou um número válido. Tente novamente.")

    operador = 0       
    
    while operador < 1 or operador > 4:              
        operador = input("Digite a operação desejada: 1= [+] | 2=[-] | 3=[*] | 4=[/]")
        
        try:
            operador = int(operador)
            if operador < 1 or operador > 4:
                print("O número digitado não está nas opções, digite novamente.")  
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 4.")  
            operador=0
            continue
        
        
    if operador == 1:

        resultado = num1 + num2

        print(f" o resultado de {num1} + {num2} é = {resultado}")
        break


    elif operador ==2:
              
        resultado = num1 - num2

        print(f" o resultado de {num1} - {num2} é = {resultado}")
        break

    elif operador ==3:
                    
        resultado = num1 * num2

        print(f" o resultado de {num1} * {num2} é = {resultado}")
        break
    
    elif operador ==4:

        if num2 == 0:
            print("Erro: divisão por zero não permitida.")  
        else:
            resultado = num1 / num2
            print(f"O resultado de {num1} / {num2} é = {resultado}")
            break

    sair = input("Você gostaria de sair? [S]im ou qualquer tecla para continuar: ").strip().upper()

