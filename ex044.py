import random

valor = random.randint(100, 10000)
print(f'R$:{valor}')

cond = int(input('Informe a condição de pagamento'
                 '[1] à vista dinheiro'
                 '[2] à vista no cartão'
                 '[3] em até 2x no cartão'
                 '[4] 3x ou mais no cartão'))

if cond == 1:
    print(f'O total de R$:{valor} saiu por R$:{valor * 0.9:.2f} com 10% de desconto!')
elif cond == 2:
    print(f'O total de R$:{valor} saiu por R$:{valor * 0.95:.2f} com 5% de desconto')
elif cond == 3:
    print(f'O total é de R$:{valor}')
elif cond == 4:
    print(f'O total de R$:{valor} saiu por R$:{valor * 1.2:.2f} com 20% de juros')
else:
    print('Condição invalida!')
