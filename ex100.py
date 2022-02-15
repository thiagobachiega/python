from random import randint
lista = []

def rand(a):
    print(f'Sorteando {a} valores da lista: ', end=' ')
    for c in range(a):
        lista.append(randint(0, 10))
    print(lista)

def somap(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma = soma + n
    print(f'Somando os valores pares da lista temos {soma}')


rand(20)
somap(lista)
