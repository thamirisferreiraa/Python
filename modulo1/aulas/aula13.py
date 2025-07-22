""" 
/*****************************************************************************

        ARGUMENTOS NOMEADOS E POSICIONAIS EM PYTHON

*****************************************************************************/

/*

1. O QUE SÃO ARGUMENTOS?

Quando chamamos uma função, passamos valores chamados **argumentos**.
Esses valores são recebidos por **parâmetros** na definição da função.

Existem dois tipos principais de argumentos em Python:

- Argumentos Posicionais
- Argumentos Nomeados (ou keyword arguments)

*/

/*

2. ARGUMENTOS POSICIONAIS

São passados na ordem em que os parâmetros foram definidos.

*/

def apresentar(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Ordem importa!
apresentar("João", 25)  # Nome: João, Idade: 25
apresentar(25, "João")  # Nome: 25, Idade: João  (resultado inesperado!)

/*

3. ARGUMENTOS NOMEADOS (KEYWORD ARGUMENTS)

Passamos os nomes dos parâmetros explicitamente.

*/

apresentar(idade=25, nome="João")  # A ordem não importa mais!
apresentar(nome="Ana", idade=30)

/*

4. MISTURANDO OS DOIS TIPOS

Podemos usar os dois tipos juntos, mas os **posicionais vêm primeiro**.

*/

def exibir_info(nome, idade, cidade):
    print(f"{nome}, {idade} anos, mora em {cidade}.")

# Correto:
exibir_info("Carlos", 40, cidade="Recife")

# Inválido (erro!): argumentos nomeados não podem vir antes dos posicionais
# exibir_info(nome="Carlos", 40, "Recife")

/*

5. VALORES PADRÃO E ARGUMENTOS NOMEADOS

Quando usamos valores padrão, podemos deixar de passar o argumento
ou alterá-lo com um argumento nomeado.

*/

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("Lúcia")  # Usa o valor padrão: Olá, Lúcia!
saudacao("Lúcia", "Oi")  # Oi, Lúcia!
saudacao(nome="Lúcia", mensagem="Bem-vinda")

/*

6. VANTAGENS DOS ARGUMENTOS NOMEADOS

- Aumentam a **clareza** da chamada.
- Permitem **escolher quais argumentos passar**, ignorando os com valor padrão.
- Evitam erros por **ordem trocada**.

*/

/*

7. EXEMPLO COMPLETO

*/

def cadastro(nome, idade=18, cidade="Desconhecida"):
    print(f"{nome}, {idade} anos, de {cidade}.")

# Chamadas possíveis:
cadastro("Joana")  # Usa valores padrão
cadastro("Rafael", 35)  # Substitui idade
cadastro("Lívia", cidade="Fortaleza")  # Usa valor nomeado para cidade

/*****************************************************************************

                EXERCÍCIOS

*****************************************************************************/

/*

1. Crie uma função que exiba o nome e a profissão de uma pessoa.
   Teste com argumentos posicionais e nomeados.

2. Crie uma função que exiba informações de um produto com nome, preço e quantidade.
   Use valores padrão para preço e quantidade.

3. Crie uma função chamada "email" que aceite um remetente, um destinatário
   e uma mensagem. Torne a mensagem opcional, com valor padrão "Sem conteúdo".

4. Crie uma função que aceite argumentos posicionais e nomeados,
   e imprima os dois separadamente.

*/



"""
#ex1
"""
def cadastro_profissao(nome, profissao):
    print(f"Nome: {nome}, Profissão: {profissao}")

cadastro_profissao(nome = "tata", profissao="programadora") 
"""
#ex2
"""def cadastro_produto(nome, preco=20.0, quantidade = 1):
        print(f"Produto: {nome}, Preço: {preco}, Quantidade: {quantidade}")

cadastro_produto("canenta", 3.0, 50)
"""

#ex3
"""rementente = input("Digite o remetente: ")
destinatario = input("Digite o destinatário: ")
mensagem = input("Digite a mensagem: ") 

def email(remetente, destinatario, mensagem="Sem conteúdo"):
    print(f"Remetente: {remetente}, Destinatário: {destinatario}, Mensagem: {mensagem}")

email(rementente, destinatario, mensagem)
"""

#ex4
def exibir_argumentos(posicionais, nomeados= 'nada'):
    print("Argumentos posicionais:", posicionais)
    print("Argumentos nomeados:", nomeados)

exibir_argumentos("primeiro", nomeados="segundo")    