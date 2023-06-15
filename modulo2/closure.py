# Closure e funções que recebem outras funções

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao},{nome}'
    return saudar

s1 = criar_saudacao('Olá', ' Diego')
s2 = criar_saudacao('Olá', ' Diego')

print(s1()) # Aqui é onde ocorre o closure, chamando a função na hora da execução
print(s2())