perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5+5?',
        'Opções': ['10', '7', '8', '9'],
        'Resposta': '10'
    },
    {
        'Pergunta': 'Quanto é 10+10?',
        'Opções': ['17', '20', '19', '15'],
        'Resposta': '20'
    },
]

for questao in perguntas:
    print(questao['Pergunta'])
    print("\n")

    for i, opcao in enumerate(questao['Opções']):
        print(f'{i+1}) {opcao}')

    print("\n")
    resposta = input("Resposta: ")

    if resposta == questao['Resposta']:
        print("Acertou!!")
        print("\n")
    else:
        print("Tente novamente.")    
        print("\n")
