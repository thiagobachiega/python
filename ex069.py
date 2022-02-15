cont18 = conth = contm = idade = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]')).lower().strip()[0]
    cad = ' '
    while cad not in 'sn':
        cad = str(input('Quer continuar?[S/N]')).lower().strip()[0]
    if idade > 18:
        cont18 = cont18 + 1
    if sexo == 'm':
        conth = conth + 1
    if sexo == 'f':
        if idade < 20:
            contm = contm + 1
    if cad == 'n':
        break
print(f'{cont18} tem mais de 18 anos, {conth} são homens e {contm} são mulheres com menos de 20 anos!')
