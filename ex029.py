velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print(f'Você foi multado em: R${(velocidade - 80) * 7.00:.2f} ')
else:
    print('Ta de boa')