print('Calculadora')

esc = 0

while esc != 5:
    num1 = float(input('Informe o primeiro valor: '))
    num2 = float(input('Informe o segundo valor: '))
    esc = int(input('Qual operação você deseja realizar?'
                    '[1]Soma'
                    '[2]Multiplicação'
                    '[3]Descobrir qual o maior'
                    '[4]informar novos números'
                    '[5]Sair do programa'))
    if esc == 1:
        print(f'A soma dos valores é {num1 + num2}')
    if esc == 2:
        print(f'A multiplicação dos valores é {num1 * num2}')
    if esc == 3:
        if num1 > num2:
            print(f'{num1} é maior!')
        else:
            print(f'{num2} é maior!')
