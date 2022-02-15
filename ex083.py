lista = []
contpa = contpf = 0

lista = input('Digite a expressão: ')

for c in lista:
    if c == '(':
        contpa = contpa + 1
    elif c == ')':
        contpf = contpf + 1

if contpa == contpf:
    print('Expressão valida!')
else:
    print('Expressão invalida!')
