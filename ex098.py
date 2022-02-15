def cont (a, b, c):
    n = 1
    if b < 0:
        n = -1
    if c == 0:
        c = 1
        if a > b:
            c = c - (c + c)
    elif c < 0:
        c = c - (c + c)
    elif a > b:
        c = c - (c + c)
    for c in range(a, b + n, c):
        print(c)


print('Contagem até 10 de 1 em 1:')
for c in range(0, 11):
    print(c, end=' ')
print()
print('Contagem de 10 até 0 de 2 em 2:')
for c in range(10, -1, -2):
    print(c, end=' ')

print()
print('Sua vez!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
cont(a, b, c)


