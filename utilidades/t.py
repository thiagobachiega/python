cont = 1
def linha():
    print('=' * 30)

def titulo(msg):
    print('=' * 30)
    print(f'{msg:^30}')
    print('=' * 30)

def opc(msg):
    global cont
    print(f'{cont} - \033[34m{msg}\033[m')
    cont = cont + 1


