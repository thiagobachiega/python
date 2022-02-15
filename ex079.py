lista = []

while True:
    esc = ' '
    num = 0
    num = int(input('Digite um número: '))
    if num in lista:
        print('O valor já foi adicionado!')
    else:
        lista.append(num)
    while esc not in 'sn':
        esc = str(input('Deseja continuar?')).lower().strip()[0]
    if esc == 'n':
        break

print(sorted(lista))
