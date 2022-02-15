lista = []
listapar = []
listaimpar = []

while True:
    num = 0
    esc = ' '
    num = int(input('Digite um número: '))
    if num == 0:
        break
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

print(f'Os valores informados foram {lista}')
print(f'Os valores pares informados foram {listapar}')
print(f'Os valores impares informados foram {listaimpar}')
