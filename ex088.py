from random import randint

lista = []
listao = []

esc = int(input('Quantos jogos você deseja fazer?'))
print(f'Sorteando {esc} jogos!'.upper())
for c in range(0, esc):
    lista = []
    while len(lista) < 6:
        num = randint(0, 60)
        while num not in lista:
            lista.append(num)
    listao.append(lista)
    #print(f'Jogo Nº{c + 1} {sorted(lista)}')

for i, l in enumerate(listao):
    print(f'Jogo nº{i + 1}: {sorted(l)}')
