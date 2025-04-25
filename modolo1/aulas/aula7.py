"""
APOSTILA – ITERÁVEIS E ITERADORES EM PYTHON
1. DEFINIÇÃO
Em Python, iteráveis e iteradores são conceitos fundamentais quando lidamos com estruturas de repetição, como o for.

Um iterável é qualquer objeto que pode ser percorrido elemento por elemento.

Um iterador é um objeto que sabe como acessar os elementos de um iterável, um por um.

2. EXEMPLOS DE ITERÁVEIS
Os tipos de dados mais comuns que são iteráveis:


lista = [1, 2, 3]
tupla = (4, 5, 6)
string = "abc"
dicionario = {"a": 1, "b": 2}
Todos eles podem ser usados em um laço for.

3. A FUNÇÃO iter()
A função iter() recebe um iterável e retorna um iterador.

Exemplo:

nomes = ["Ana", "Bia", "Carlos"]
it = iter(nomes)  # transforma a lista em um iterador
4. A FUNÇÃO next()
A função next() recebe um iterador e retorna o próximo item da sequência. Quando os itens acabam, ela levanta um erro StopIteration.

Exemplo:

print(next(it))  # Ana
print(next(it))  # Bia
print(next(it))  # Carlos
# print(next(it))  # StopIteration
5. COMPARANDO for VS iter/next
O for usa iter() e next() nos bastidores.

# Jeito comum
for nome in nomes:
    print(nome)

# Equivalente com iter e next
it = iter(nomes)
while True:
    try:
        nome = next(it)
        print(nome)
    except StopIteration:
        break
6. CRIANDO UM ITERADOR MANUALMENTE
Você pode criar sua própria classe iteradora implementando os métodos __iter__() e __next__().

Exemplo:

class Contador:
    def __init__(self, limite):
        self.atual = 0
        self.limite = limite

    def __iter__(self):
        return self  # um iterador deve retornar a si mesmo

    def __next__(self):
        if self.atual >= self.limite:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

# Usando nosso iterador
for numero in Contador(3):
    print(numero)  # imprime 0, 1, 2
7. USO COMUNS
Ler arquivos linha por linha.

Processar grandes volumes de dados.

Geradores (funções com yield) também criam iteradores.

8. RESUMO

Conceito	Significado
Iterável	Pode ser percorrido (tem __iter__())
Iterador	Objeto com __next__() e __iter__()
iter(obj)	Retorna um iterador a partir de um iterável
next(obj)	Retorna o próximo item do iterador
StopIteration	Exceção lançada quando os itens acabam
Se quiser, posso montar esse conteúdo em PDF ou PowerPoint no mesmo estilo da sua apostila de C. Quer que eu prepare isso?







Dito por si:
me expkique como funciona o range()


Dito pelo ChatGPT:
Claro! Vamos entender o range() passo a passo, como se fosse uma apostila didática:

FUNÇÃO range() EM PYTHON
1. DEFINIÇÃO
A função range() cria uma sequência de números inteiros, usada principalmente em laços for.

Ela não gera uma lista diretamente, mas sim um objeto especial iterável que vai fornecendo os números conforme necessário (economizando memória).

2. SINTAXE


range(início, fim, passo)
início: número onde a sequência começa (opcional – padrão é 0)

fim: número onde a sequência para (não é incluído!)

passo: intervalo entre os números (opcional – padrão é 1)

3. EXEMPLOS
Exemplo 1: Apenas o fim

for i in range(5):
    print(i)
Saída:


0
1
2
3
4
Começa em 0 e vai até 4 (o 5 não entra).

Exemplo 2: Início e fim

for i in range(2, 6):
    print(i)
Saída:

2
3
4
5
Exemplo 3: Usando passo
python

for i in range(1, 10, 2):
    print(i)
Saída:

1
3
5
7
9
Exemplo 4: Passo negativo (contagem regressiva)


for i in range(10, 0, -1):
    print(i)
Saída:


10
9
8
...
1
4. CONVERTENDO EM LISTA (só para visualizar)
Se quiser ver todos os valores de um range de uma vez:

print(list(range(4)))  # [0, 1, 2, 3]
5. RESUMO

Código	Resultado
range(5)	0 até 4
range(2, 6)	2, 3, 4, 5
range(1, 10, 2)	1, 3, 5, 7, 9
range(10, 0, -1)	10 até 1 (decrescendo)



"""


for i in range(10):
    if i == 2:
        print('i é igual a 2, pulando...')
        continue

    if i == 8:
        print('i é igual 8 seu else não executará')
        break

    for j in range(1,3):
        print(f'i: {i}, j: {j}')

else:
    print('for completo com sucesso')