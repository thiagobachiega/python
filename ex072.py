num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
valor = 0
while True:
    valor = int(input('Informe um número de 0 a 20: '))
    if valor > 0 and valor < 20:
        break
    if valor < 0 or valor > 20:
        print('Valor invalido, tente novamente!')
print(f'{valor} por extenso é {num[valor]}')
