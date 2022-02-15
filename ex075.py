n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um: '))
n4 = int(input('Ultimo eu juro: '))

contpar = 0

numeros = (n1, n2, n3, n4)

print(numeros)

print(f'O numero 9 aparece {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição!')
else:
    print('Não há valor 3!')

for n in numeros:
    if n % 2 == 0:
        contpar = contpar + 1

print(f'Há {contpar} números pares!')