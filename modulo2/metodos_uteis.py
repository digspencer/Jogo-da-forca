# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

#Criando um dicionário

pessoa = {
    'nome': 'Diego',
    'nome_meio': 'Paulino',
    'nome_final': 'Souza',
    'idade': 33
}

print(len(pessoa))
print(pessoa.keys())

for valor in pessoa.values():
    print(valor)

for chave, indice in pessoa.items():
    print(chave, indice)