def leiaint(n):
    while True:
        try:
            n = int(input(n))
        except(ValueError, TypeError):
            print('ERRO: Informe um valor inteiro valido!')
            continue
        else:
            return n


def leiafloat(n):
    while True:
        try:
            n = float(input(n))
        except(ValueError, TypeError):
            print('ERRO: informe um número real valido!')
            continue
        else:
            return n


numi = leiaint('Informe um número inteiro: ')
numr = leiafloat('Informe um número real: ')
print(f'Você digitou o número inteiro: {numi} e o número real: {numr}')
