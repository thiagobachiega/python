pessoas = {'nome':' ','sexo':' ','idade':' '}
lista = []
soma = media = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    while pessoas['sexo'] not in 'mf':
        pessoas['sexo'] = str(input('Sexo: ')).lower().strip()[0]
        if pessoas['sexo'] not in 'mf':
            print('Valor invalido, digite apenas M ou F!')
    pessoas['idade'] = int(input('Idade: '))
    soma = soma + pessoas['idade']
    lista.append(pessoas.copy())
    pessoas = {'nome':' ','sexo':' ','idade':' '}
    esc = ' '
    while esc not in 'sn':
        esc = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
        if esc not in 'sn':
            print('Valor invalido, digite apenas S ou N!')
    if esc == 'n':
            break

print(f'Ao todo foram {len(lista)} pessoas cadastradas')
media = soma / len(lista)
print(f'A media de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'f':
        print(p["nome"])
print('As pessoas acima da média de idade foram: ', end='')
for pe in lista:
    if pe['idade'] > media:
        print(pe['nome'])



