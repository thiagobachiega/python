def ajuda(fun):
    while True:
        titulo('SISTEMA DE AJUDA PYFDEU')
        fun = (input('Digite o nome da função: '))
        if fun == 'exit':
            break
        help(fun)
def titulo(msg):
    print(f'\033[34m=' * len(msg))
    print(f'{msg:^20}')
    print(f'=' * len(msg))


print(ajuda(len))