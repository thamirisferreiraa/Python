"""
/*****************************************************************************

            EXERCÍCIOS

*****************************************************************************

OBS.: Escreva os programas no estilo modular. Use funções quando necessário.

1 - Crie uma lista com 5 nomes. Imprima apenas os que começam com a letra "a".

2 - Peça ao usuário para digitar 5 números e guarde-os em uma lista.
    Em seguida, mostre:
    a) O maior valor
    b) O menor valor
    c) A média dos valores

3 - Crie uma lista de 10 números. Remova todos os valores pares e mostre o resultado.

4 - Use uma lista para simular uma fila:
    a) Adicione elementos ao final da fila com append()
    b) Remova do início com pop(0)
    c) Mostre a fila atual após cada operação

5 - Simule um carrinho de compras:
    a) O usuário digita o nome de produtos até escrever "sair"
    b) Mostre a lista final com todos os itens do carrinho

7 - Dada a lista abaixo, crie uma nova lista contendo apenas os nomes com 5 letras ou mais:
    nomes = ["ana", "bia", "carla", "daniel", "eva", "felipe"]

8 - Escreva uma função que recebe uma lista de números e retorna outra lista com os quadrados desses números.

*****************************************************************************/
"""
 #ex1
"""

lista = ["thamiris", "carolina", "diego", "kevin", "ademir"]

for nome in lista:
    if 'a' in nome:
        print(nome)

"""

#ex2
"""       
lista = []
soma = 0 
for i in range(5):
    n = int(input(f"Digite um {i+1}º número: "))
    lista.append(n)
    soma += n

print("Lista final: ", lista)    

lista.sort()
print(f"O maior numero da lista é: {lista[-1]}") 
print(f"O menor numero da lista é: {lista[0]}")

media = soma / 5
print(f"A média dos numeros digitados é de: {media}")

"""

#ex3
"""
lista = []

for i in range(10):
    n = int(input(f"Digite um {i+1}º número: "))
    lista.append(n)

lista_impar = []

for num in lista:
    if num % 2 != 0:
       lista_impar.append(num)

print(f"A lista completa é: {lista}")
print(f"A lista sem os números pares é: {lista_impar}")        
"""

#ex4
"""
lista = []
while True:
    print("MENU")

    print("-------------------")

    print("1- Adicionar itens a lista")
    print("2- Remover um item")
    print("3- Sair")

    opcao = int(input("Digite o numero da operação: "))

    if opcao == 1:
        item = input("Digite o nome do item: ")
        lista.append(item)
        print(f"Lista: {lista}")
    elif opcao == 2:
        remover = input("Digite o nome do item para excluir: ")
        if remover in lista:
            print("Item encontrado")
            lista.remove(remover)
            print(f"Lista: {lista}")
        else:
            print(f"O item {remover} não foi encontrado na lista")    
    elif opcao == 3:
        print("Saindo...")
        exit(0)
    else:
        print("A opção digitada não existe, tente novamente")
"""

#ex5
"""
lista = []

while True:
    print("MENU")

    print("-------------------")

    print("1- Adicionar itens ao carinho")
    print("2- Remover um item")
    print("3- Sair")

    opcao = int(input("Digite o número da operação: "))

    if opcao == 1:
        item = input("Digite o nome do produto para adicionar ao carrinho: ") 
        lista.append(item)
        print(f"Carinho: {lista}")
    elif opcao == 2:
        item = input("Digite o nome do produto que gostaria de remover do carinho: ")

        if item in lista:
            print("Produto encontrado")
            lista.remove(item)
            print(f"Carinho: {lista}")
        else:
            print(f"O item {item} não foi encontrado no carrinho")   
    elif opcao == 3:    
        print("Saindo...")
        exit(0)
    else:
        print("A opção digitada não existe, tente novamente")   

"""

#ex6
"""
nomes = ["ana", "bia", "carla", "daniel", "eva", "felipe"]
nome_cinco = []

for nome in nomes:
    if len(nome) >= 5:
        nome_cinco.append(nome)

print(f"Os nomes com 5 ou mais letras são: {nome_cinco}")
"""

#ex7

numeros = []
numeros_quadrado = []

for i in range(5):
    n = int(input(f"Digite o {i+1} numero: "))

    numeros.append(n)


for num in numeros:
    numeros_quadrado.append(num ** 2)

print(f"A lista digitada foi: {numeros}")  
print(f"A lista ao quadrado ficou: {numeros_quadrado}")
