# Closure e funções que recebem outras funções

def criar_saudacao(saudacao, nome):
    return f'{saudacao},{nome}'

s1 = criar_saudacao('Olá', ' Diego')
s2 = criar_saudacao('Olá', ' Diego')

print(s1)
print(s2)