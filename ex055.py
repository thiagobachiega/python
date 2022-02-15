maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}º pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso foi de {menor}KG e o maior peso foi de {maior}KG')


