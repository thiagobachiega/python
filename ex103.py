def jogador(nome, gols):
    if nome == '':
        if gols == '':
            return f'O <nao informado> fez 0 gols no campeonato.'
        else:
            return f'O <nao informado> fez {gols} gols no campeonato.'
    elif gols == '':
        return f'O {nome} fez 0 gols no campeonato.'
    return f'O {nome} fez {gols} gols no campeonato.'


nome = str(input('Informe o nome do jogador: '))
gols = str(input('Número de gols: '))
print(jogador(nome, gols))
