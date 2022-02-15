num = soma = cont = maior = menor = 0
esc = ''

while esc != 'n':
    num = int(input('Informe um valor: '))
    esc = str(input('Deseja continuar? [S/N]')).lower()
    soma = soma + num
    cont = cont + 1
    menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / cont
print(f'A média dos {cont} valores informados foi de {media}')
print(f'O menor valor foi {menor} e o maior foi {maior}')
