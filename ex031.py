viagem = float(input('Quantos KM tem a viagem?'))

if viagem <= 200:
    print(f'A passagem irá custar: R${viagem * 0.50:.2f}')
else:
    print(f'A viagem irá custar: R${viagem * 0.45:.2f}')