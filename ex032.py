ano = int(input('Ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Não Bissexto')