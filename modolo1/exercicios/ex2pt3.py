#ex3

nome = input("Digite seu nome: ")
 
lent_nome = len(nome)

if lent_nome <= 4 and lent_nome != 0:
    print("Seu nome é curto")
elif 5 <= lent_nome <= 6:
    print("Seu nome é normal")
elif lent_nome > 6:
    print("Seu nome é muito grande") 
else:
     print("Seu nome não pode ter 0 letras, digite novamete")          
