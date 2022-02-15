casa = int(input('Informe o valor da casa: '))
parcelamento = int(input('Informe em quantos anos será feito parcelamento: '))
salario = int(input('Informe o seu salário: '))

parc = casa / (parcelamento * 12)
porc = salario * 0.3

if parc > porc:
    print(f'Você não pode financiar a casa em {parcelamento} anos')
else:
    print(f'Você pode financiar a casa em {parcelamento} anos')
