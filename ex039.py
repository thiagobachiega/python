from datetime import datetime

nasc = int(input('Informe a data de nascimento: '))

data = int(datetime.today().strftime('%Y'))
idade = data - nasc

print(f'Quem nasceu em {nasc} tem {idade} em {data}')

if idade < 18:
    saldo = 18 - idade
    print(f'Você vai ter que se alistar em {saldo} anos')
elif idade == 18:
    print(f'Você deve se alistar esse ano!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos!')




