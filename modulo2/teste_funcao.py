# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi = multiplicar(10, 2, 3, 4, 5, 6)

def num_par(numero):
    par = numero % 2 == 0

    if par:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(num_par(multi))