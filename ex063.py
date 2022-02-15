num1 = 0
num2 = 1
num3 = 0

termos = int(input('Quantos termos você deseja exibir?'))

cont = 0

while cont < termos:
    if cont == 0:
        print(num1, num2, end=' ')

    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3, end=' ')

    cont = cont + 1