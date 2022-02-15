termo = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

decimo = termo + (10 - 1) * razao

'''for c in range(termo, decimo + razao, razao):
    print(c)'''
c = termo

while c < decimo + razao:
    print(c)
    c = c + razao