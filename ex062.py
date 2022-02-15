primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
quant = 10
total = 0
while cont <= quant:
    print(f'{termo} > ', end='')
    termo = termo + razão
    cont = cont + 1
    if cont > quant:
        mais = int(input('Quantos valores quer mostrar a mais?'))
        quant = quant + mais
        total = total + mais

print(f'Foram exibidas um total de {total} progressões!')
print('FIM')