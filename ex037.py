numero = int(input('Escreva um número: '))
conversor = int(input('''Escolha um metodo de conversão:
[1]Binário
[2]Hexadecimal
[3]Octal
'''))

if conversor == 1:
    print(bin(numero))
elif conversor == 2:
    print(hex(numero))
elif conversor == 3:
    print(oct(numero))
else:
    print('Erro! informe um valor valido!')



