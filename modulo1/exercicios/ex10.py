def verificador(num1):
    if num1 % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    

numero = int(input("Digite um número: "))    

print(verificador(numero))
