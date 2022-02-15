matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = somac = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]'))
        if l == 1 and matriz[1][c] > maior:
            maior = matriz[1][c]

        elif matriz[l][c] % 2 == 0:
            soma = soma + matriz[l][c]

for l in range(0, 3):
    somac = somac + matriz[l][2]











print(matriz)
print(f'A soma dos valores pares é de: {soma}')
print(f'A soma dos valores na terceira coluna é: {somac}')
print(f'O maior valor na segunda linha é: {maior}')

