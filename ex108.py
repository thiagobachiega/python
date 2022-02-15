import moeda

num = float(input('Informe um valor: '))
print(f'O dobro de {num} é: {moeda.conv(moeda.dobro(num))}')
print(f'A metade de {num} é: {moeda.conv(moeda.metade(num))}')
aumento = int(input('Quantos % de aumento?'))
print(f'{num} com {aumento}% de aumento fica: {moeda.conv(moeda.aumento(num, aumento))}')
diminuir = int(input('Quantos % de decressimo?'))
print(f'{num} com {diminuir}% de decressimo fica: {moeda.conv(moeda.diminuir(num, diminuir))}')