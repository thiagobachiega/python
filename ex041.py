from datetime import date

ano = int(input('Informe o ano de nascimento do atleta: '))
data = int(date.today().year)
idade = data - ano

if idade <= 9:
    print(f'O Atleta tem {idade} anos e está na categoria mirim!')
elif idade <= 14 and idade > 9:
    print(f'O Atleta tem {idade} anos e está na categoria infantil!')
elif idade <= 19 and idade > 14:
    print(f'O Atleta tem {idade} anos e está na categoria junior!')
elif idade <= 25 and idade > 19:
    print(f'O Atleta tem {idade} anos e está na categoria senior!')
elif idade > 25:
    print(f'O Atleta tem {idade} anos e está na categoria master! ')
else:
    print('Informe um valor valido!')