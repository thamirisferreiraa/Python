"""
/*****************************************************************************

            LISTA DE EXERCÍCIOS – TUPLAS, EMPACOTAMENTO E DESEMPACOTAMENTO

*****************************************************************************/

/* 

1. Crie uma tupla com os nomes de 5 frutas. Mostre a segunda e a última fruta.

2. Crie uma tupla com 3 números inteiros. Calcule e exiba a soma deles.

3. Dada a tupla (3.14, 2.71, 1.41), desempacote seus valores em três variáveis
   chamadas `pi`, `e` e `raiz` e exiba cada uma.

4. Escreva uma função que receba dois números e retorne uma tupla contendo:
   - a soma
   - a subtração
   - a multiplicação
   - a divisão

5. Dada a lista [1, 2, 3, 4, 5], converta para tupla e imprima o tipo de dado.

6. Dada a tupla de nomes abaixo, use um laço `for` com `enumerate` para exibir
   o índice e o nome:
   nomes = ("ana", "bia", "carla", "daniel")

7. Crie uma tupla com valores repetidos e use o método `count()` para mostrar
   quantas vezes o número 7 aparece.

8. Crie uma tupla com 6 valores e use fatiamento para exibir:
   - os três primeiros
   - os três últimos
   - os valores de índice par

9. Use desempacotamento com `*` para guardar todos os nomes, menos o primeiro,
   em uma lista chamada `resto`:
   exemplo:
       nomes = ("lucas", "ana", "maria", "joao")
       primeiro, *resto = nomes

10. Desafio: Escreva um programa que leia nome, idade e profissão do usuário,
    empacote esses dados em uma tupla, e depois desempacote em variáveis para
    exibir uma frase como:
    "Fulano tem 30 anos e trabalha como engenheiro."

*****************************************************************************/

"""

#ex1

"""trupla = ("banana", "maçã", "melão", "uva", "abacaxi")

print(trupla[0])
print(trupla[4])"""

#ex2

"""trupla = (10, 20, 30)

num1, num2, num3 = trupla

soma = num1 + num2 + num3

print(f"A soma dos 3 numeros {num1} + {num2} + {num3} = {soma}")"""

#ex3
"""
trupla = (3.14, 2.71, 1.41)

pi, e, raiz = trupla

print(f"O valor de pi é: {pi}")
print(f"O valor de e é: {e}")
print(f"O valor da raiz é: {raiz}")
"""

#ex4
"""
def operacoes(x,y):
    return( x + y, x - y, x * y, x / y )

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = operacoes(a,b)

print(f"Soma: {resultado[0]}")
print("Subtração:", resultado[1])
print("Multiplicação:", resultado[2])
print("Divisão:", resultado[3])
"""

#ex5
"""
lista = [1, 2, 3, 4, 5]
trupla = tuple(lista)

for numero in trupla:
    print(type(numero))
"""

#ex6
"""
nomes = ("ana", "bia", "carla", "daniel")

for indice, nome in enumerate(nomes):
    print(indice, nome)
    """

#ex7
"""
tupla = (7, 10, 5, 6, 7, 2, 3, 7, 7, 8, 9, 7)

print(f"O número 7 apareceu {tupla.count(7)} vezes")
"""

#ex8
"""
tupla = (7, 10, 5, 6, 7, 2)

for indice, numero in enumerate(tupla):
    if indice <= 2:
        print(f"Indice: {indice}, Número: {numero} \n")
    else:
        print(f"Indice: {indice}, Número: {numero} \n")

    if indice % 2 == 0:
        print(f"Numeros com o indice par: ")       
        print(f"Indice: {indice}, Número: {numero} \n")

"""

#ex9
"""
nomes = ("lucas", "ana", "maria", "joao")
primeiro, *resto = nomes
resto = tuple(resto)

print(primeiro)
print(resto)
"""

#ex10 - desafio

nome = input("Digite seu nome: ") 
idade = int(input("\nDigite sua idade: "))
profissao = input("\nDigite sua profissão:")

dados = (nome, idade, profissao)

nome, idade, profissao = dados

print(f"{nome} tem {idade} e trabalha como {profissao}")

