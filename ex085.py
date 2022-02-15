lista = [[],[]]

for c in range(0, 6):
    num = 0
    num = int(input('Informe um número: '))
    if num % 2 == 0:
        lista[0].insert(c, num)
    else:
        lista[1].insert(c, num)

lista[0].sort()
lista[1].sort()
print(lista)