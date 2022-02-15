num = int(input('Digite um número: '))
total = 0

'''if num % 2 == 0 or num % 3 == 0 and num != 2 and num != 3:
    print('Não é primo!')
else:
    print('É primo!')'''

for c in range(1, num +1):
    if num % c == 0:
        total = total + 1
if total > 2:
    print('Não é primo')
else:
    print('É primo')

