def dobro(n, f=True):
    dobro = n * 2
    if f == True:
        return f'R${dobro:.2f}'.replace('.', ',')
    return dobro

def metade(n, f=True):
    metade = n / 2
    if f == True:
        return f'R${metade:.2f}'.replace('.', ',')
    return metade

def aumento(n, p, f=True):
    aumento = n * (1 + (p / 100))
    if f == True:
        return f'R${aumento:.2f}'.replace('.', ',')
    return aumento

def diminuir(n, p, f=True):
    diminuir = n - (n * (p / 100))
    if f == True:
        return f'R${diminuir:.2f}'.replace('.', ',')
    return diminuir

def conv(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(n, pa, pd):
    resumo = {}
    resumo['dobro'] = dobro(n)
    resumo['metade'] = metade(n)
    resumo['aumento'] = aumento(n, pa)
    resumo['diminuir'] = diminuir(n, pd)
    print(f'=' * 30)
    print(f'{"Resumo":^30}')
    print(f'=' * 30)
    print(f'Preço analisado:\t{conv(n)}')
    print(f'Dobro do preço:\t{resumo["dobro"]}')
    print(f'Aumento de {pa}%:\t{resumo["aumento"]}')
    print(f'Decressimo de {pd}%:\t{resumo["diminuir"]}')
    print(f'=' * 30)
