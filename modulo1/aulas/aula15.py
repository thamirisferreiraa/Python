"""/*****************************************************************************

        *ARGS — ARGUMENTOS POSICIONAIS VARIÁVEIS EM PYTHON

*****************************************************************************/

/*

1. O QUE É *args?

`*args` é usado em funções quando **não sabemos quantos argumentos** 
posicionais serão passados.

A palavra "args" é uma convenção (pode ser outro nome), mas o `*` é obrigatório.

*/

def mostrar_numeros(*args):
    print(args)

mostrar_numeros(1, 2, 3)     # (1, 2, 3)
mostrar_numeros(10)          # (10,)
mostrar_numeros()            # ()

/*

2. COMO FUNCIONA?

Todos os argumentos posicionais são recebidos em uma **tupla**.

*/

def somar_tudo(*args):
    total = 0
    for numero in args:
        total += numero
    print("Soma:", total)

somar_tudo(1, 2, 3, 4)  # Soma: 10

/*

3. NOMES ALTERNATIVOS

O nome `args` pode ser qualquer um, mas o `*` deve estar presente.

*/

def listar(*itens):
    for item in itens:
        print("-", item)

listar("maçã", "banana", "uva")

/*

4. COMBINAÇÃO COM PARÂMETROS FIXOS

Podemos misturar parâmetros normais com `*args`. O `*args` deve vir **por último**.

*/

def saudacoes(mensagem, *nomes):
    for nome in nomes:
        print(f"{mensagem}, {nome}!")

saudacoes("Olá", "Ana", "Bia", "Carlos")

/*

5. DESEMPACOTAMENTO DE LISTAS/VALORES

Podemos passar uma lista como se fosse vários argumentos com `*`.

*/

def soma(*args):
    return sum(args)

numeros = [1, 2, 3]
print(soma(*numeros))  # 6

/*

6. DIFERENÇA ENTRE * E **

- `*args`: vários argumentos **posicionais** (sem nome).
- `**kwargs`: vários argumentos **nomeados** (com chave=valor).
  (kwargs é tratado em outra apostila)

*/

/*

7. EXEMPLO COMPLETO

*/

def media(*numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

print("Média:", media(8, 7, 9))  # Média: 8.0
print("Média:", media())        # Média: 0

/*****************************************************************************

                EXERCÍCIOS

*****************************************************************************/

/*

1. Crie uma função que receba vários números e retorne o maior.

2. Crie uma função que receba vários nomes e os imprima em ordem alfabética.

3. Crie uma função que simule uma lista de compras com `*args`.
   Ela deve imprimir item por item.

4. Crie uma função chamada `multiplicar` que receba vários números
   e retorne o resultado da multiplicação entre eles.

5. Crie uma função que receba uma mensagem e vários nomes,
   e imprima "<mensagem>, <nome>!" para cada nome.

*/

"""

#ex1
"""
def numeros_retorno():
    lista_numeros = []
    while True:
        numero = int(input("Digite um numero (digite 0 para sair):"))

        if numero == 0:
            break

        lista_numeros.append(numero)

    if lista_numeros:
        return max(lista_numeros)
    else:
        return "Nenhum número foi digitado além de 0."
       

print(f"O maior número digitado é: {numeros_retorno()}")      
"""
#ex2
"""
def nome_retorno():

    lista = []

    while True:
        nome = input("Digite um nome (digite sair para sair): ")      

        if nome == 'sair':
            break

        lista.append(nome)
    if lista:
        lista.sort()
        return lista
    else:
        return "Nenhum nome foi digitado" 

print(f"Ordem alfabatica dos nomes digitados \n {nome_retorno()}")                  
"""

#ex3
"""
lista = []
while True:
    item = input("Digite um item (digite sair para sair):")

    if item == 'sair':
        break

    lista.append(item)


def imprimir(*args):
    for item in lista:
        print(f"Item: {item}")


imprimir(lista)
"""

#ex4
"""def multiplicador():
    resultado = 1
    while True:
        numero = int(input("Digite um numero ou '0' para sair: "))

        if numero == 0:
            break

        resultado *= numero

    if resultado != 1:
        return resultado
    else:
        return "Nenhum número foi digitado" 

print(f"O resultado da multiplicação foi: {multiplicador()}")
"""

#ex5

def saudacoes(mensagem, *args):
    for nome in args:
        print(f"{mensagem}, {nome}")

mens = input("Digite sua mensagem: ") 

lista_nomes = []

while True: 
    nome = input("Digite um nome ou 'sair' para sair: ")

    if nome == 'sair':
        break

    lista_nomes.append(nome)

saudacoes(mens, *lista_nomes)
