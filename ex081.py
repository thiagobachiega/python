lista = []
cont = 0
while True:
    num = 0
    num = int(input('Digite um número: '))
    if num in lista:
        print('O Valor já foi adicionado anteriormente!')
    else:
        lista.append(num)
        cont = cont + 1
    esc = ' '
    while esc not in 'sn':
        esc = str(input('Deseja continuar?'))
    if esc == 'n':
        break

print(f'Foram inseridos ao todo {cont} valores!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 está na {lista.count(5) + 1}º posição!')
else:
    print('O valor 5 não foi digitado')