num = 1

while num > 0:
    cont = 1
    num = int(input('Informe um número para ver a sua tabuada: '))
    while cont < 11:
        if num < 0:
            break
        print(f'{num} x {cont} = {num * cont}')
        cont = cont + 1
