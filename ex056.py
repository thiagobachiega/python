somaidade = 0
media = 0
maisvelho = 0
mnova = 0

for c in range(1, 5):
    print(f'{c}º Pessoa')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M]/[F]: ').upper()

    somaidade = somaidade + idade

    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        hmaisvelho = nome

    if sexo == 'F' and idade < 20:
        mnova = mnova + 1

media = somaidade / 4

print(f'A média de idade do grupo é de {media} anos!')
print(f'O homem mais velho é {hmaisvelho} com {maisvelho} anos!')
print(f'Há {mnova} mulheres com menos de 20 anos no grupo!')



