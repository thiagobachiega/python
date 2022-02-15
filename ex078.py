lista = []

for c in range(0, 5):
    lista.append(int(input('Informe um valor: ')))


print(lista)

menor = maior = contmaior = contmenor =  0

for e, c in enumerate(lista):
    if e == 0:
        menor = maior = c
    if c > maior:
        maior = c
        contmaior = e

    if c < menor:
        menor = c
        contmenor = e

if c == maior:
    print(f'As posiçãoes do maior numero são:{e}')

print(f'O maior valor foi {maior} encontrado na {contmaior + 1}º posição e o menor valor foi {menor} encontrado na {contmenor + 1}º posição!')
