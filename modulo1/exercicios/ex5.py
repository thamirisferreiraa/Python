"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = "perfume"
letras_acertadas = '' 
tentativas = 0

while True:

    entrada = input("Digite uma letra: ")
    tentativas += 1

    if len(entrada) > 1:
        print("Digite apenas uma letra")
        continue
    
    if entrada in palavra_secreta:
               letras_acertadas += entrada

    palavra_formada = ''

    for letras_secretas in palavra_secreta:
            if letras_secretas in letras_acertadas:
               palavra_formada += letras_secretas
            else:
                palavra_formada += '*'

    print(f"Palavra formada: {palavra_formada}")            
    
    if palavra_formada == palavra_secreta:
        print("Parabéns, você acertou a palavra!!!")
        print(f"A palavra era: {palavra_formada}")
        print(f"Total de tentativas: {tentativas}")
        break
        exit(0)