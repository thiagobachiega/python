def fatorial(n, show=True):
    '''
    Calcula o fatorial de um número.
    :param n: Numero a ser calculado.
    :param show: Exibe ou não o calculo. True para exibir, false para não exibir.
    :return: O fatorial do número informado.
    '''
    print(f'O fatorial de {n} é: {n}', end=' ')
    for c in range(n - 1, 0, -1):
        if show == True:
            print(f'x {c}', end=' ')
        n = n * c
    print(f'= {n}')


fatorial(5, show=True)
help(fatorial)