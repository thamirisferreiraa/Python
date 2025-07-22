"""/*****************************************************************************

        CLOSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES EM PYTHON

*****************************************************************************/

/*

1. FUNÇÃO RETORNANDO OUTRA FUNÇÃO

Em Python, funções podem ser **retornadas** de dentro de outras funções.

Isso é possível porque funções são objetos de primeira classe.

*/

def criar_mensagem():
    def mensagem():
        print("Olá! Essa é uma função interna.")
    return mensagem

# Usando a função retornada
func = criar_mensagem()
func()  # Olá! Essa é uma função interna.

/*

2. FUNÇÕES INTERNAS

Podemos definir funções dentro de outras funções.

*/

def saudacao():
    def bom_dia():
        print("Bom dia!")
    def boa_noite():
        print("Boa noite!")

    bom_dia()
    boa_noite()

saudacao()

/*

3. CLOSURE: O QUE É?

Closure é quando uma **função interna** **lembra** as variáveis do seu **escopo externo** mesmo depois que a função externa já terminou de executar.

*/

def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar  # retorna a função interna

# Criando uma closure
dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))   # 10
print(triplo(5))  # 15

/*

4. COMO FUNCIONA?

Mesmo depois que `multiplicador` terminou, a função interna `multiplicar` ainda lembra do valor de `fator`.

Isso é uma closure: a função **fecha** sobre as variáveis que estavam no escopo em que foi criada.

/*

5. EXEMPLO COM TEXTO

*/

def prefixador(prefixo):
    def adicionar(texto):
        return f"{prefixo} {texto}"
    return adicionar

bom_dia = prefixador("Bom dia")
boa_noite = prefixador("Boa noite")

print(bom_dia("João"))     # Bom dia João
print(boa_noite("Maria"))  # Boa noite Maria

/*

6. VANTAGENS DAS CLOSURES

✅ Mantêm "estado" sem usar variáveis globais  
✅ Permitem **criar funções configuráveis**  
✅ Muito úteis em programação funcional e em decorators

*/

/*

7. CLOSURE NÃO É A MESMA COISA QUE RETORNAR FUNÇÃO

- Toda closure retorna uma função.
- Nem toda função retornada é closure (só se lembrar de variáveis externas).

*/

/*

8. FUNÇÃO COMO FÁBRICA DE FUNÇÕES

Closures funcionam como **fábricas de funções personalizadas**.

*/

def contador(inicio=0):
    numero = inicio
    def proximo():
        nonlocal numero
        numero += 1
        return numero
    return proximo

c1 = contador()
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3

c2 = contador(100)
print(c2())  # 101
print(c2())  # 102

"""