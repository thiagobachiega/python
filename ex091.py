from random import randint
from operator import itemgetter
ranking = {}
jogadores = {'jogador1':randint(0, 6),
             'jogador2':randint(0, 6),
             'jogador3':randint(0, 6),
             'jogador4':randint(0, 6)}

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=' * 36)
for c, v in enumerate(ranking):
    print(f'O {ranking[c][0]} ficou em {c + 1}º com {ranking[c][1]} pontos!')
