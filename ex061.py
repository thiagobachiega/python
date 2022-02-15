'''termo = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
quant = int(input('Qual o tamanho da progressão?'))

c = termo
cont = 1

while cont <= quant:
    print(c)
    c = c + razao
    cont = cont + 1
    if cont > quant:
        quant = int(input('Quantas a mais?'))
        quant = quant + c'''



















#versão guanabara

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
