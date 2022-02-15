salario = float(input('Qual o salário do funcionário?: '))
porcentagem = float(input('Quantos % de aumento?: '))
aumento = salario + (salario * porcentagem /100)
print('O aumento vai ser de {:.2f}R$ para {:.2f}R$'.format(salario, aumento))
