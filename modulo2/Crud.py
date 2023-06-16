pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz'
pessoa['sobrenome'] = 'Miranda'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])

