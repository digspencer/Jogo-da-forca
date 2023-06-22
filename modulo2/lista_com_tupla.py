p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Souza',
}

tupla = (('nome', 'novo valor'), ('idade', 30)) # Tupla de tuplas
lista = [['nome', 'novo valor'], ['idade', 30]] # Lista de Listas

p1.update(tupla)
print(p1)
