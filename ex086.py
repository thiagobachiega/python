'''lista = [[], [], []]

for c in range(0, 9):
    num = int(input(f'Informe um valor para {lista[0]}: '))
    if c < 3:
        lista[0].append(num)
    elif c < 6:
        lista[1].append(num)
    else:
        lista[2].append(num)

print(lista[0])
print(lista[1])
print(lista[2])'''

#versão guanabara

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]'))

print(matriz)


