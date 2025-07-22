"""
/*****************************************************************************

        MÉTODOS ÚTEIS DOS DICIONÁRIOS (dict) EM PYTHON

*****************************************************************************/

/*

1. LEMBRETE: O QUE É UM DICIONÁRIO?

Dicionário é uma estrutura de dados que armazena pares **chave:valor**.

Exemplo:

*/

aluno = {
    "nome": "Ana",
    "idade": 22,
    "curso": "Python"
}

/*

2. .get(chave, valor_padrao)

Retorna o valor da chave. Se a chave não existir, retorna o valor padrão.

*/

print(aluno.get("nome"))          # Ana
print(aluno.get("nota", "N/A"))   # N/A

/*

3. .keys()

Retorna todas as **chaves** do dicionário.

*/

print(aluno.keys())  # dict_keys(['nome', 'idade', 'curso'])

/*

4. .values()

Retorna todos os **valores** do dicionário.

*/

print(aluno.values())  # dict_values(['Ana', 22, 'Python'])

/*

5. .items()

Retorna uma lista de tuplas (chave, valor).

*/

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

/*

6. .update(outro_dicionario)

Atualiza o dicionário com os dados de outro.

*/

aluno.update({"idade": 23, "nota": 9.5})
print(aluno)

/*

7. .pop(chave)

Remove e retorna o valor de uma chave. Se a chave não existir, dá erro.

*/

nota = aluno.pop("nota")
print("Nota removida:", nota)

/*

8. .popitem()

Remove e retorna o **último** item inserido (em versões recentes do Python).

*/

ultimo = aluno.popitem()
print("Removido:", ultimo)

/*

9. .setdefault(chave, valor)

Retorna o valor da chave. Se não existir, insere com o valor informado.

*/

aluno.setdefault("cidade", "São Paulo")
print(aluno["cidade"])  # São Paulo

/*

10. .clear()

Remove todos os itens do dicionário.

*/

aluno.clear()
print(aluno)  # {}

/*

11. len(dicionario)

Retorna a quantidade de itens no dicionário.

*/

dados = {"a": 1, "b": 2}
print(len(dados))  # 2

/*****************************************************************************

                EXERCÍCIOS

*****************************************************************************/

/*

1. Crie um dicionário com dados de um aluno (nome, idade, curso).
   Use `.get()` para acessar um campo que não existe.

2. Crie um dicionário e use `.update()` para adicionar uma nova chave.

3. Use `.pop()` para remover uma chave de um dicionário.

4. Percorra um dicionário com `.items()` e imprima as chaves e valores.

5. Crie um dicionário vazio e adicione elementos com `.setdefault()`.

6. Crie um dicionário com 3 elementos e remova todos com `.clear()`.

7. Use `.keys()`, `.values()` e `.items()` em um dicionário e imprima os resultados.

8. Crie uma função que recebe um dicionário e imprime quantos itens ele tem.

*/



"""