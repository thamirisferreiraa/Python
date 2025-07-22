"""
/*****************************************************************************

               SPLIT(), JOIN() E STRIP() 

*****************************************************************************/

/*

1. split()

O método split() divide uma string em partes, usando um separador. 
Por padrão, o separador é o espaço.

Formato:
    string.split(separador)

Retorna: uma lista de strings.

*/

# Exemplo:
frase = "Python é incrível"
palavras = frase.split()
print(palavras)  # ['Python', 'é', 'incrível']

# Com separador personalizado:
data = "01/05/2025"
partes = data.split("/")
print(partes)  # ['01', '05', '2025']

/*

2. join()

O método join() faz o inverso do split(): junta os elementos de uma lista
em uma única string, usando um separador.

Formato:
    separador.join(lista)

*/

# Exemplo:
nomes = ["ana", "bia", "carla"]
texto = ", ".join(nomes)
print(texto)  # "ana, bia, carla"

# Com hífen:
codigo = ["2025", "05", "01"]
data_formatada = "-".join(codigo)
print(data_formatada)  # "2025-05-01"

/*

3. strip()

O método strip() remove espaços em branco (ou outros caracteres) 
do início e do fim da string.

Existem também:
    - lstrip(): remove só da esquerda
    - rstrip(): remove só da direita

*/

# Exemplo:
texto = "   Olá mundo!   "
limpo = texto.strip()
print(limpo)  # "Olá mundo!"

# Removendo outro caractere:
url = "www.exemplo.com///"
limpo = url.rstrip("/")
print(limpo)  # "www.exemplo.com"

/*
"""

