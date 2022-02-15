from utilidades import t

cadastro = {}
cadastros = [{'nome': 'ana', 'idade': 18}, {'nome': 'paulo', 'idade': 20}]


def menu():
    while True:
        t.titulo('MENU PRINCIPAL')
        t.opc('Ver pessoas cadastradas')
        t.opc('Cadastro')
        t.opc('Deletar')
        t.opc('Sair')
        t.linha()
        t.cont = 1
        try:
            n = int(input('Escolha uma opção: '))
        except(ValueError, TypeError):
            print('ERRO DIGITE UMA OPÇÃO VALIDA!')
        else:
            if n == 1:
                for v, c in enumerate(cadastros):
                    print(f'{v} - {cadastros[v]["nome"]}, {cadastros[v]["idade"]}')
            elif n == 2:
                cadastro['nome'] = str(input('Informe o nome: '))
                cadastro['idade'] = int(input('Informe a idade: '))
                print('Cadastro realizado com sucesso!')
                cadastros.append(cadastro.copy())
            elif n == 3:
                rmv = int(input('Qual item deseja remover?[999]para cancelar'))
                if rmv == 999:
                    break
                cadastros.pop(rmv)
            elif n == 4:
                t.titulo('Finalizando!')
                break
            else:
                print(f'\033[34mERRO, INFORME UMA OPÇÃO VALIDA!\033[m')
