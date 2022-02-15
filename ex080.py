lista = []

for c in range(0, 5):
    num = 0
    num = (int(input('Digite um número: ')))
    if num in lista:
        print('O valor já foi adicionado anteriormente!')
    elif c == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num < lista[pos]:
                lista.insert(pos, num)
                break
            pos = pos + 1
print(lista)
