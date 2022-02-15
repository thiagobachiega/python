nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media > 6:
    print(f'Sua média é {media}!')
    print('Aprovado!')
elif media < 6 and media > 5:
    print(f'Sua média é {media}!')
    print('Você está de recuperação!')
else:
    print(f'sua média é {media}!')
    print('Você está reprovado!')
