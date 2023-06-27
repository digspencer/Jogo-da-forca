pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
} 

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# ** Faz a extração de dentro do dicionário
pessoas_completa = {**pessoa, **dados_pessoa}

print(pessoas_completa)

#Kwargs são argumentos nomeados

def mostro_argumentos_nomeados(*args, **kwargs):
    print(kwargs)

mostro_argumentos_nomeados(nome='Joana', qlq=123)

config = { 
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**config)