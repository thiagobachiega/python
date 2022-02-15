lista = []
listap = []
soma = cont = info = 0

while True:

    nome = str(input('Informe o nome do aluno: '))
    listap.append(nome)
    while True:
        escc = ' '
        nota = float(input(f'Informe a {cont + 1}º nota do aluno: '))
        listap.append(nota)
        cont = cont + 1
        soma = soma + nota
        while escc not in 'sn':
            escc = str(input('Deseja continuar?')).lower()[0]
        if escc == 'n':
            break
    media = soma / cont
    listap.append(media)
    cont = 0
    soma = 0
    print(listap)
    lista.append(listap[:])
    listap = []
    esc = ' '
    while esc not in 'sn':
        esc = str(input('Deseja inserir outro aluno?')).lower()[0]

    if esc == 'n':
        break

print('Nº NOME    MÉDIA')
for i, l, in enumerate(lista):
    print(f'{i} {lista[i][0]} {lista[i][len(lista[i]) - 1]:6}')

while True:
    info = int(input('Deseja ver a nota de qual aluno?'))
    if info == 999:
        break
    print(f'{lista[info][1:-1]}')
