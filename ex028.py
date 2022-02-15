import random

num = random.randint(0,5)

esc = int(input('Escolha um numero de 0 a 5: '))

if esc == num:
    print('Você venceu!!')
else:
    print('O computador venceu!!')

print(num)