num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))

if num1 > num2:
    print(f'{num1} é maior!')
elif num2 > num1:
    print(f'{num2} é maior!')
elif num1 == num2:
    print('Os numeros são iguais!')
else:
    print('Erro!')