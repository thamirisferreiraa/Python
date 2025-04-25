primeiro_valor= input("Digite um número: ")
segundo_valor= input("Digite outro número: ")

valor1 = int(primeiro_valor)
valor2 = int(segundo_valor)

if valor1 > valor2:
    print(f"O número {valor1} é maior que o número {valor2}")
elif valor1 < valor2:
    print(f" O número {valor2} é maior que o número {valor1}")
else:
    print("Os números são iguais")