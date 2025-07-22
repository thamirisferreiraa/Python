"""
Faça uma lista de comprar com listas 
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erro de indices inexistentes na lista
"""

lista = []
while True:
    print("             MENU                ")
    print("----------------------------------")
    print("1 - Inserir dados")
    print("2 - Apagar dados")
    print("3 - Listar dados")
    print("4 - Sair")
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:

        item = input("\nDigite o item que deseja adicionar: ")
        lista.append(item)
        
    elif opcao == 2:

        dado = int(input("\nDigite o indice do item que deseja excluir: "))

        if 0 <= dado < len(lista):
            print("\nIndice encontrado, removendo item...")
            del lista[dado]
            print(f"\nItem {lista[dado]} removido!!")
        else:
            print("Indice não encontrado ou inexistente, tente novamente")
    elif opcao == 3:

        if len(lista) == 0:
            print("\nA lista está vazia!!")
        else:    
            print("\nItens da lista: ")

            for i, item in enumerate(lista):
                print(f"Indide: {i}, Item: {item}")

    elif opcao == 4:
        print("Saindo...")
        exit(0)
    else:
        print("Opção inválida, tente novamente")    

    
        
        