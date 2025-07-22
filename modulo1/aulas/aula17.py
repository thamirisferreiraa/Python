"""
/*****************************************************************************

                    DICIONÁRIOS EM PYTHON

*****************************************************************************/

/*

1. O QUE É UM DICIONÁRIO?

Dicionário é uma estrutura de dados **chave-valor**.

Cada item tem:

➡️ Uma **chave (key)** única  
➡️ Um **valor (value)** associado

É muito usado para representar objetos, cadastros, configurações etc.

Sintaxe:
    dicionario = {chave: valor, chave2: valor2}

*/

aluno = {
    "nome": "Ana",
    "idade": 22,
    "curso": "Python"
}

/*

2. ACESSANDO VALORES

Usamos a chave entre colchetes `[]` ou o método `.get()`.

*/

print(aluno["nome"])     # Ana
print(aluno.get("curso"))  # Python

# .get() evita erro se a chave não existir:
print(aluno.get("nota", "Não cadastrada"))  # Não cadastrada

/*

3. MODIFICANDO VALORES

*/

aluno["idade"] = 23
aluno["curso"] = "Data Science"

/*

4. ADICIONANDO NOVOS PARES

*/

aluno["nota"] = 9.5

/*

5. REMOVENDO ELEMENTOS

*/

del aluno["nota"]           # Remove uma chave
aluno.pop("curso")          # Também remove
aluno.clear()               # Apaga tudo

/*

6. DICIONÁRIOS VAZIOS

*/

d1 = {}             # Forma 1
d2 = dict()         # Forma 2

/*

7. PERCORRENDO UM DICIONÁRIO

*/

dados = {"nome": "Carlos", "idade": 30, "cidade": "SP"}

for chave in dados:
    print(chave, "->", dados[chave])

# ou

for chave, valor in dados.items():
    print(chave, ":", valor)

/*

8. MÉTODOS ÚTEIS

*/

print(dados.keys())     # Todas as chaves
print(dados.values())   # Todos os valores
print(dados.items())    # Todos os pares

/*

9. DICIONÁRIOS ANINHADOS

Podemos ter dicionários dentro de dicionários.

*/

alunos = {
    "joao": {"idade": 20, "nota": 8},
    "maria": {"idade": 21, "nota": 9}
}

print(alunos["joao"]["nota"])  # 8

/*

10. USO COM LISTAS

Listas podem conter dicionários — ótimo para cadastros.

*/

pessoas = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Bia", "idade": 25}
]

for pessoa in pessoas:
    print(pessoa["nome"], "-", pessoa["idade"])

*****************************************************************************/

/*

                EXERCÍCIOS

*/

/*

1. Crie um dicionário com informações de uma pessoa (nome, idade, cidade).

2. Acesse e imprima o valor da chave "cidade".

3. Adicione uma nova chave chamada "profissão".

4. Crie uma função que receba um dicionário de aluno e imprima todos os dados.

5. Faça uma lista com 3 dicionários de alunos, cada um com nome e nota.
   Imprima apenas os nomes dos alunos com nota maior que 7.

6. Crie um dicionário onde a chave é o nome de um produto e o valor é o preço.
   Mostre o produto mais caro.

7. Escreva uma função que recebe um dicionário e retorna a média dos valores numéricos.

8. Crie um sistema simples de cadastro de pessoas (nome, idade), onde os dados
   ficam armazenados em uma lista de dicionários.

*/




"""
"""
#ex1

pessoa = {
    "nome": "Thamiris",
    "idade": 19,
    "cidade": "santos",
}

#ex2

print(pessoa["cidade"])

#ex3

pessoa["profissao"] = "Análista de dados"

for chave in pessoa:
    print(chave, ":", pessoa[chave])


"""
#ex4
"""
def exibir_dados(aluno):
    for chave, valor in aluno.items():
        print(chave, ":", valor)

dados = {
    "nome": "carol",
    "idade": 20,
    "media": 8.5
}        

exibir_dados(dados)
"""

#ex5
"""
alunos = [
    {"nome": "Pedro", "nota": 5.5},
    {"nome": "Ananda", "nota": 7.5},
    {"nome": "yasmin", "nota": 8},
    {"nome": "ingrid", "nota": 1}
]

for aluno in alunos:
    if aluno["nota"] > 7:
        print(aluno["nome"], "-", aluno["nota"])
 """     

#ex6  
"""
produtos = [
    {"produto": "iphone 12", "valor": 3000}, 
    {"produto": "iphone 13", "valor": 7000},
    {"produto": "iphone 13", "valor": 4000}
]

maior = produtos[0]

for produto in produtos:
    if produto["valor"] > maior["valor"]:
        maior = produto
        
print("O produto mais caro é:")
print(f"{maior["produto"]} - R$ {maior['valor']}")
"""

#ex7
"""
dicionario = [
    {"valor": 20},
    {"valor": 55},
    {"valor": 7},
    {"valor": 90},
    {"valor": 45},
    {"valor": 1}
]

def media(lista):
    soma = 0
    quant = 0
    for item in lista:
        soma += item["valor"]
        quant += 1

    md = soma / quant
    print(f"Média: {md:.2f}")    

media(dicionario)        
"""

#EX8

dicionario = []

while(1):
    print("            MENU\n")
    print("----------------------------")
    print("1- adicionar cadastro:")
    print("2- mostrar lista")
    print("3- sair")
    opcao = int(input("Digite a opção"))

    if opcao == 1:
        nome = input("digite o nome: ")
        idade = int(input("digite a idade: "))

        dicionario.append({"nome": nome, "idade": idade})
    elif opcao == 2:
        print("lista\n")
        for pessoa in dicionario:
            print(pessoa["nome"], "-", pessoa["idade"], "anos")    
    elif opcao == 3:
        print("saindo")
        exit(0)
    else:
        print("opcao invalida")        