def printar(a, b, c):
    print('Primeiro')
    print('Segundo')
    print('Terceiro')

printar(1, 2, 3)

def cade_seu_nome(nome):
    print(f'Olá {nome}')

cade_seu_nome("Matheus")


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)