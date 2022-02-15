soma = 0
cont1000 = 0
menor_valor = 0
produtob = ''
valor_produto = 0
cont = 0
while True:
    esc = ' '
    nome_produto = str(input('Informe o nome do produto: '))
    valor_produto = int(input('Preço:'))
    cont = cont + 1
    while esc not in 'sn':
        esc = str(input('Quer continuar?[S/N]')).lower().strip()[0]
    if cont == 1:
        menor_valor = valor_produto
    if valor_produto < menor_valor:
        produtob = nome_produto
        menor_valor = valor_produto
    if valor_produto > 1000:
        cont1000 = cont1000 + 1
    soma = soma + valor_produto


    if esc == 'n':
        break

print(f'O valor total da compra foi de R${soma}!')
print(f'Tiveram {cont1000} produtos com valor superior a R$1000')
print(f'O produto mais barato foi um(a) {produtob} de R${menor_valor}')