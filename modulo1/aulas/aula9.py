"""
/*****************************************************************************

            TUPLAS, EMPACOTAMENTO E DESEMPACOTAMENTO EM PYTHON

*****************************************************************************/

/*

1. TUPLAS - DEFINIÇÃO

Tuplas são estruturas de dados sequenciais, assim como listas, mas **imutáveis**.
Isso significa que, uma vez criada, seus elementos **não podem ser alterados**.

Tuplas usam parênteses `()` e são ideais para armazenar dados fixos.

*/

# Exemplo de tuplas:
coordenadas = (10, 20)
dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta")

# Tupla com 1 elemento (note a vírgula):
um_elemento = (42,)

/*

2. ACESSANDO ELEMENTOS

Assim como listas, os elementos de uma tupla podem ser acessados por índice:

*/

print(coordenadas[0])  # imprime 10
print(dias_semana[2])  # imprime quarta

/*

3. TUPLAS SÃO IMUTÁVEIS

Tentar alterar ou remover um item de uma tupla causará erro:

*/

dias = ("seg", "ter", "qua")
# dias[0] = "domingo"  # ERRO! Tuplas não permitem alteração

/*

4. DESEMPACOTAMENTO DE TUPLAS

É possível atribuir os elementos de uma tupla diretamente a variáveis separadas:

*/

coordenadas = (100, 200)
x, y = coordenadas

print(f"x = {x}, y = {y}")  # x = 100, y = 200

/*

5. EMPACOTAMENTO DE VALORES

Também podemos fazer o inverso: atribuir vários valores em uma única tupla:

*/

a = 5
b = 10
tupla = (a, b)

# ou diretamente:
tupla = 5, 10  # empacotamento implícito

print(tupla)  # (5, 10)

/*

6. EMPACOTAMENTO/DESEMPACOTAMENTO MÚLTIPLO

*/

# Desempacotando vários valores:
dados = ("alice", 30, "engenheira")
nome, idade, profissao = dados

# Empacotando vários valores:
pessoa = nome, idade, profissao

/*

7. USO DO * (ASTERISCO) NO DESEMPACOTAMENTO

O `*` permite capturar múltiplos valores em uma variável, como uma lista:

*/

valores = (1, 2, 3, 4, 5)

a, b, *resto = valores
print(a)       # 1
print(b)       # 2
print(resto)   # [3, 4, 5]

/*

8. CONVERSÃO ENTRE LISTA E TUPLA

Você pode converter de uma para outra:

*/

lista = [10, 20, 30]
tupla = tuple(lista)       # [10, 20, 30] → (10, 20, 30)

nova_lista = list(tupla)   # (10, 20, 30) → [10, 20, 30]

/*

9. USOS COMUNS DE TUPLAS

- Armazenar constantes
- Retornar múltiplos valores de uma função
- Iterar com `enumerate()`

*/

# Retorno múltiplo:
def ponto():
    return (3, 4)

x, y = ponto()

# Enumerate com desempacotamento:
nomes = ["ana", "bia", "carol"]
for i, nome in enumerate(nomes):
    print(f"{i}: {nome}")

/*

10. MÉTODOS ÚTEIS DAS TUPLAS

Tuplas têm poucos métodos, pois são imutáveis:

- count(x): conta quantas vezes x aparece
- index(x): retorna o índice da primeira ocorrência de x

*/

cores = ("azul", "verde", "vermelho", "azul")
print(cores.count("azul"))   # 2
print(cores.index("verde"))  # 1

/*****************************************************************************

            FIM - TUPLAS, EMPACOTAMENTO E DESEMPACOTAMENTO

*****************************************************************************/
"""
