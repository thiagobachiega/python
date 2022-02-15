from operator import itemgetter
jogador = {}
gols = []
totg = 0

jogador['nome'] = str(input('Qual o nome do jogador?: '))
part = int(input('Quantas partidas ele jogou? '))

for c in range(0, part):
    gols.append(int(input(f'Quantos gols ele marcou na {c + 1}º partida?')))

for c in gols:
    totg = totg + c

jogador['gols'] = gols
jogador['total'] = totg

print(jogador)
print('=' * 36)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 36)
print(f'O jogador {jogador["nome"]} jogou {part} partidas!')

for c, v in enumerate(jogador['gols']):
    print(f'Na {c+1}º partida ele marcou {v} gols')

print(f'Foi um total de {jogador["total"]} gols!')



