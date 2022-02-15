from datetime import date
data = date.today().year

pessoa = {}

pessoa['nome'] = str(input('Informe o nome: '))
pessoa['nascimento'] = int(input('Informe o ano de nascimento: '))
pessoa['idade'] = data - pessoa['nascimento']
pessoa['carteira'] = int(input('Informe o numero da carteira (digite 0 se não possuir!): '))
if pessoa['carteira'] != 0:
    pessoa['anocont'] = int(input('Informe o ano de contratação: '))
    pessoa['salario'] = float(input('Informe o valor do salário: '))
    pessoa['aposentadoria'] = pessoa['anocont'] - pessoa['nascimento'] + 40

print(pessoa)

for k, v in pessoa.items():
    print(f'{k} tem o valor: {v}')