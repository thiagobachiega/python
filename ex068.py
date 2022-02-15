import random
num = numc = soma = 0
result = ''
cont = 0

while True:
    num = int(input('Escolha um numero de 1 a 10!'))
    esc = str(input('Par ou Impar?')).lower()
    numc = random.randint(1, 10)
    soma = num + numc
    print(soma)
    if soma % 2 == 0:
        result = 'par'
        print('Par')
    else:
        result = 'impar'
        print('Impar')

    if esc == result:
        cont = cont + 1
        print('Você venceu!')
        print(f'Você venceu {cont} vezes!')
    else:
        print('Você perdeu')
        print(f'Você venceu {cont} vezes, mais sorte da próxima!')
        break


