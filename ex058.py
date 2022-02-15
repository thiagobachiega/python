'''import random

num = random.randint(0,5)

esc = int(input('Escolha um numero de 0 a 5: '))

if esc == num:
    print('Você venceu!!')
else:
    print('O computador venceu!!')

print(num)'''

import random

esc = 0
num = 1
tentativas = 0

while esc != num:
    num = random.randint(1, 10)
    esc = int(input('Tente advinhar o número de 1 a 10 que o computador escolheu: '))
    print(esc, num)
    if esc != num:
        tentativas = tentativas + 1
        print('Número errado, tente novamente!')
print(f'Parabéns você acertou com {tentativas} tentativas!')
