'''
Retorno de valores das funções
'''

def soma(x, y):
    return x + y


soma1 = soma(2, 4)
soma2 = soma(3, 3)

#No caso com o 'return' ele retorna para dentro da função o valor
print(soma1 + soma2)

# * São argumentos não nomeados
a, b, *resto = 1, 2, 3, 4
print(a, b, *resto) 

def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = 1, 2, 3, 4, 5
somar(*numeros)
# A função 'sum()' é o que nos conhecemos como soma
print(sum(numeros))