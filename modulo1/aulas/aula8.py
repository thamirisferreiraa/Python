"""
/*****************************************************************************

                                 LISTAS 

*****************************************************************************/

/*

1. DEFINIÇÃO

Listas são estruturas de dados do tipo sequencial que permitem armazenar
múltiplos valores em uma única variável. As listas em Python são mutáveis, ou
seja, seus elementos podem ser alterados após a criação.

Elas podem conter valores de qualquer tipo: inteiros, strings, floats, outras
listas, etc.

*/

# Exemplo:
numeros = [10, 20, 30, 40, 50]
nomes = ["ana", "bia", "carlos"]

# lista mista
dados = [1, "texto", 3.14, True]

/*

2. ACESSANDO ELEMENTOS

Para acessar elementos da lista, usa-se o índice (posição), que começa em 0.

Formato:
    lista[indice]

*/

print(numeros[0])  # imprime 10
print(nomes[2])    # imprime carlos

/*

3. MODIFICANDO ELEMENTOS

Como listas são mutáveis, podemos alterar valores diretamente pelo índice.

*/

numeros[1] = 25  # muda o valor da posição 1 de 20 para 25
print(numeros)   # imprime [10, 25, 30, 40, 50]

/*

4. ADICIONANDO ELEMENTOS

Existem 3 formas comuns:

- append(): adiciona no final
- insert(): insere em uma posição específica
- extend(): adiciona todos os elementos de outra lista

*/

lista = [1, 2, 3]

lista.append(4)        # [1, 2, 3, 4]
lista.insert(1, 10)    # [1, 10, 2, 3, 4]
lista.extend([5, 6])   # [1, 10, 2, 3, 4, 5, 6]

/*

5. REMOVENDO ELEMENTOS

- pop(): remove por índice (ou o último se nenhum índice for passado)
- remove(): remove o primeiro valor correspondente
- del: remove pelo índice
- clear(): remove todos os elementos

*/

itens = ["a", "b", "c", "d"]

itens.pop()        # remove "d"
itens.pop(1)       # remove "b"
itens.remove("a")  # remove "a"
del itens[0]       # remove "c"
itens.clear()      # lista vazia

/*

6. PERCORRENDO LISTAS

Para percorrer os elementos de uma lista, usamos o laço for:

*/

numeros = [10, 20, 30]

for n in numeros:
    print(n)  # imprime cada número

/*

7. TAMANHO DA LISTA

Para saber quantos elementos uma lista possui, usamos a função len():

*/

lista = [1, 2, 3, 4]
print(len(lista))  # imprime 4

/*

8. FATIAMENTO DE LISTAS

É possível obter partes da lista (sub-listas) usando a notação de fatiamento:

Formato:
    lista[início:fim:passo]

- início: onde começa (inclusivo)
- fim: onde termina (exclusivo)
- passo: intervalo (opcional)

9. OUTRAS FUNÇÕES ÚTEIS

- sorted(lista): retorna uma nova lista ordenada (sem modificar a original)
- sort(): ordena a lista original (em ordem crescente por padrão)
- reverse(): inverte a ordem dos elementos da lista
- in: verifica se um elemento está presente na lista
- index(): retorna o índice da primeira ocorrência de um valor
- count(): conta quantas vezes um valor aparece

*/

valores = [3, 1, 4, 1, 5, 9, 2]

print(sorted(valores))     # [1, 1, 2, 3, 4, 5, 9]
valores.sort()             # valores agora é [1, 1, 2, 3, 4, 5, 9]
valores.reverse()          # valores agora é [9, 5, 4, 3, 2, 1, 1]

print(4 in valores)        # True
print(valores.index(5))    # 1 (primeira ocorrência do número 5)
print(valores.count(1))    # 2 (duas ocorrências do número 1)

"""