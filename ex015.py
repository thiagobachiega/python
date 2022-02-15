dia = int(input('Por quantos dias o carro ficou alugado?: '))
km = float(input('Quantos KM foram rodados?: '))

pdia = dia * 60
pkm = km * 0.15
aluguel = pdia + pkm

print('O carro foi alugado por {}dias e rodou {}Km, o valor do aluguel ficou em {}R$'.format(dia, km, aluguel))
