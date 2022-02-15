listao = []
listat = []
cont = mleve = mpesado = 0

while True:
    listat.append(str(input('Informe o nome do paciente: ')))
    listat.append(float(input('Informe o peso do paciente: ')))
    if len(listao) == 0:
        mleve = mpesado = listat[1]
    else:
        if listat[1] > mpesado:
            mpesado = listat[1]
        elif listat[1] < mleve:
            mleve = listat[1]
    listao.append(listat[:])
    listat.clear()
    cont = cont + 1
    esc = ' '
    while esc not in 'sn':
        esc = str(input('Deseja continuar?[s/n]'))
    if esc == 'n':
        break

print(listao)

print(f'Foram informados {len(listao)} valores!')

print(f'O peso mais leve foi de {mleve} de: ', end='')
for p in listao:
    if p[1] == mleve:
        print(f'[{p[0]}]', end=' ')
print(f'O peso mais pesado foi de {mpesado} de: ', end='')
for p in listao:
    if p[1] == mpesado:
        print(f'[{p[0]}]', end=' ')


