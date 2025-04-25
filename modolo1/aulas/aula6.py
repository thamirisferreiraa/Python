"""
1. DEFINIÇÃO
Em Python, iteráveis e iteradores são conceitos fundamentais quando lidamos com estruturas de repetição, como o for.

Um iterável é qualquer objeto que pode ser percorrido elemento por elemento.

Um iterador é um objeto que sabe como acessar os elementos de um iterável, um por um.

2. EXEMPLOS DE ITERÁVEIS
Os tipos de dados mais comuns que são iteráveis:

python
Copiar
Editar
lista = [1, 2, 3]
tupla = (4, 5, 6)
string = "abc"
dicionario = {"a": 1, "b": 2}
Todos eles podem ser usados em um laço for.

3. A FUNÇÃO iter()
A função iter() recebe um iterável e retorna um iterador.

Exemplo:
python
Copiar
Editar
nomes = ["Ana", "Bia", "Carlos"]
it = iter(nomes)  # transforma a lista em um iterador
4. A FUNÇÃO next()
A função next() recebe um iterador e retorna o próximo item da sequência. Quando os itens acabam, ela levanta um erro StopIteration.

Exemplo:
python
Copiar
Editar
print(next(it))  # Ana
print(next(it))  # Bia
print(next(it))  # Carlos
# print(next(it))  # StopIteration
5. COMPARANDO for VS iter/next
O for usa iter() e next() nos bastidores.

python
Copiar
Editar
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
python
Copiar
Editar
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


"""

texto = iter('Thamiris')

iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
