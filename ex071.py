print(20 * '-')
print('WELCOME TO DA BANK')
print(20 * '-')
num = int(input('Quanto você quer sacar? R$'))
rest1 = rest2 = rest3 = 0

print(f'Total de {num // 50} notas de R$50')
rest1 = num % 50

print(f'Total de {rest1 // 20} notas de R$20')
rest2 = rest1 % 20

print(f'Total de {rest2 // 10} notas de R$10')
rest3 = rest2 % 10

print(f'Total de {rest3 // 1} notas de R$1')
print(30 * '-')
print('COME BACK TO DA BANK SOON')
print(30 * '-')


