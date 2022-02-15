'''num = int(input('Digite um número para ver a sua tabuada:'))
print('-'*12)
print('{} x 1 = {:^10}'.format(num, num * 1))
print('{} x 2 = {:^10}'.format(num, num * 2))
print('{} x 3 = {:^10}'.format(num, num * 3))
print('{} x 4 = {:^10}'.format(num, num * 4))
print('{} x 5 = {:^10}'.format(num, num * 5))
print('{} x 6 = {:^10}'.format(num, num * 6))
print('{} x 7 = {:^10}'.format(num, num * 7))
print('{} x 8 = {:^10}'.format(num, num * 8))
print('{} x 9 = {:^10}'.format(num, num * 9))
print('{} x 10 = {:^9}'.format(num, num * 10))
print('-'*12)'''

num = int(input('Digite um número para ver a sua tabuada: '))
for c in range(0, 11):
    print(f'{num} x {c} = {num * c}')