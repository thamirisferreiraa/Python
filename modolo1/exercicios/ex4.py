frase = 'O Python é uma linguagem de programação multiparadigma. Pyhton foi criado por Guido Van Rossum'

i = 0
apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase): 
    letra_atual = frase[i]

    i+= 1

    if letra_atual == ' ':
        continue

    cont_letra = frase.count(letra_atual)

    if apareceu_mais < cont_letra:
        apareceu_mais = cont_letra
        letra_apareceu_mais = letra_atual

    

print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais}" que apareceu {apareceu_mais} vezes')

    
