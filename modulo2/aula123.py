p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Souza',
}

print(p1['nome']) 
print(p1['sobrenome']) 
print(p1.get('nome', 'Não Existe')) # Caso o segundo parametro não existir ele retorna 

p1.pop('nome') # O método pop apaga a chave que foi passada como parametro (del)
print(p1.popitem()) #Apaga a última chave do dicionário
p1.update({ 'nome' : 'novo valor', 'idade' : 30}) # Ese método atualiza as chaves existentes e cria uma nova chave
