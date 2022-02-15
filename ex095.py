jogador = {}
jogadores = []
gols = []
totg = 0
escc = ' '

while True:
    jogador['nome'] = str(input('Qual o nome do jogador?: '))
    part = int(input('Quantas partidas ele jogou? '))

    for c in range(0, part):
        gols.append(int(input(f'Quantos gols ele marcou na {c + 1}º partida?')))

    for c in gols:
        totg = totg + c

    jogador['gols'] = gols
    jogador['total'] = totg
    jogadores.append(jogador.copy())
    jogador = {}
    gols = []
    totg = 0
    esc = ' '
    esc = str(input('Deseja continuar? [S/N]'))
    if esc == 'n':
        break

print('=' * 36)
print(jogadores)

print('cod nome        gols        total')
for c, v in enumerate(jogadores):
    print(f'{c:5<} {jogadores[c]["nome"]:12} {jogadores[c]["gols"]} {jogadores[c]["total"]:5}')

while True:
    escc = ' '
    escc = int(input('Deseja informar os dados de qual jogador? informe o código! [999] para parar!'))
    if escc == 999:
        break
    for c, v in enumerate(jogadores[escc]["gols"]):
        print(f'No {c + 1}º jogo marcou {v} gols')




'''for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 36)
print(f'O jogador {jogador["nome"]} jogou {part} partidas!')

for c, v in enumerate(jogador['gols']):
    print(f'Na {c+1}º partida ele marcou {v} gols')

print(f'Foi um total de {jogador["total"]} gols!')'''
