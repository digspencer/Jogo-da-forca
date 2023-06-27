# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

# Lista Comprehension

lista = [numero for numero in range(10)]
print(lista)

lista2 = [item * 2 for item in range(10)]
print(lista2)