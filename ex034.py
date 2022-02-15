salario = int(input('Informe o salário: '))

if salario <= 1250:
    print(f'Você ganhou um aumento de 15%, R$:{salario + 15/100 * salario}')
else:
    print(f'Você ganhou um aumento de 10%, R$:{salario + 10/100 * salario}')