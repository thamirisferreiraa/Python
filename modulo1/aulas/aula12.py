"""
/*****************************************************************************

                FUNÇÕES EM PYTHON

*****************************************************************************/

/*

1. DEFINIÇÃO

Função é um bloco de código que só é executado quando for chamado.
Permite **organizar**, **reutilizar** e **modularizar** o programa.

Formato básico:

def nome_da_funcao(parâmetros):
    bloco de código

*/

/* 

2. EXEMPLO DE FUNÇÃO SIMPLES

*/

def saudacao():
    print("Olá! Bem-vindo ao programa.")

# Chamada da função:
saudacao()

/*

3. FUNÇÕES COM PARÂMETROS

Podemos passar valores para a função através de parâmetros.

*/

def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} + {b} = {resultado}")

soma(3, 5)  # Chamada com argumentos

/*

4. FUNÇÕES COM RETORNO

A função pode devolver um valor usando **return**.

*/

def quadrado(x):
    return x ** 2

resultado = quadrado(4)
print(f"O quadrado é {resultado}")

/*

5. PARÂMETROS PADRÃO

Podemos definir valores padrão para os parâmetros, tornando-os opcionais.

*/

def saudacao(nome="usuário"):
    print(f"Olá, {nome}!")

saudacao("Ana")    # Olá, Ana!
saudacao()        # Olá, usuário!

/*

6. FUNÇÃO COM VÁRIOS ARGUMENTOS (*args)

Podemos passar uma quantidade indefinida de argumentos.

*/

def listar_nomes(*nomes):
    for nome in nomes:
        print(nome)

listar_nomes("Ana", "Bia", "Carlos")

/*

7. FUNÇÃO COM VÁRIOS PARÂMETROS NOMEADOS (**kwargs)

Permite receber vários parâmetros com nome.

*/

def perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

perfil(nome="Ana", idade=30, cidade="São Paulo")

/*

8. ESCOPO DE VARIÁVEIS

- Variáveis criadas dentro da função: **escopo local**.
- Variáveis fora da função: **escopo global**.

*/

x = 10  # variável global

def funcao():
    x = 5  # variável local
    print(x)  # 5

funcao()
print(x)  # 10

/*

9. FUNÇÃO LAMBDA (FUNÇÃO ANÔNIMA)

São funções de uma linha, úteis para tarefas simples.

Formato:
    lambda parâmetros: expressão

*/

quadrado = lambda x: x ** 2
print(quadrado(3))  # 9

/*

10. DOCSTRINGS

Comentários que explicam o que a função faz.

*/

def soma(a, b):
    
    Esta função soma dois números.
    
    return a + b

print(soma(2, 3))

/*****************************************************************************

                EXERCÍCIOS

*****************************************************************************/

/*

1. Crie uma função que receba um número e retorne se ele é par ou ímpar.

2. Crie uma função que receba dois números e retorne a soma, subtração,
   multiplicação e divisão (como tupla).

3. Crie uma função que receba um nome e imprima: "Bem-vindo, <nome>!".

4. Crie uma função que receba um número indeterminado de nomes e imprima cada um.

5. Crie uma função que receba uma lista de números e retorne a média.

6. Crie uma função que verifique se um número é primo.

7. Crie uma função que peça ao usuário um número e devolva o seu fatorial.

8. Crie uma função que recebe uma frase e retorna a quantidade de palavras
   (use split()).

9. Crie uma função que recebe um CPF (como string) e retorne formatado:
   xxx.xxx.xxx-xx.

10. Crie uma função anônima (lambda) que calcule a área de um círculo.

*/

"""