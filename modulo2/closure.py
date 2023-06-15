# Closure e funções que recebem outras funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia ')
falar_boa_noite = criar_saudacao('Boa noite')

lista = ['Diego', 'Maria', 'Luiz']

for nome in lista:
    print(falar_bom_dia(nome),nome)
    print(falar_boa_noite(nome),nome)