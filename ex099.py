'''def maior(lst):
    for c in range(0, len(lst)):
        if c == 0:
            maior = lst[c]
        if lst[c] > maior:
            maior = lst[c]
    print(maior)


lista = []

while True:
    valor = int(input('Informe os valores, digite 999 para parar!: '))
    if valor == 999:
        break
    lista.append(valor)

print(lista)
maior(lista)'''


def maior(* num):
    cont = maiorr = 0
    for n in num:
        if cont ==0:
            maiorr = n
        else:
            if n > maiorr:
                maiorr = n
        cont = cont + 1
    print(f'Foram informados {cont} valores')
    print(f'E o maior valor foi {maiorr}')


maior(1, 5, 10, 7)
maior(0, 8, 2, 22, 34, 60)

