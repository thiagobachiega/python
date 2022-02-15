frase = str(input('Digite uma frase')).strip().lower()

lista = frase.split()
frasee = ''.join(lista)

fraser = frasee[::-1]

print(fraser)

if fraser == frasee:
    print('Palindromo!')
else:
    print('Não é um palindromo!')