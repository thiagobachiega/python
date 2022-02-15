tupla = ('Abacate', 'Cenoura', 'Banana')

for palavra in tupla:
    print(f'As vogais dá palavra {palavra} são: ', end='')

    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'-{letra}-', end='')

