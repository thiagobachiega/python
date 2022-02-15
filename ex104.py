def val(n):
    if n.isnumeric() == True:
        return f'Você digitou o número: {n}'
    else:
        return f'Erro, informe um valor valido!'

n = input('Informe um número: ').strip()
print(val(n))