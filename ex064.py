num = 0

soma = 0
cont = 0

while num != 999:
    num = int(input('Digite 999 para parar!'))
    if num != 999:
        soma = soma + num
        cont = cont + 1
print(f'A soma dos valores foi de {soma} e o total de valores somados foi de {cont}')
