nome = input('Digite seu nome:')
print(f'Seu nome maiusculo: {nome.upper()}')
print(f'Seu nome minusculo: {nome.lower()}')

nomes = nome.split()

print('Seu nome tem {} letras'.format(len(''.join(nomes))))

print(f'Seu primeiro nome tem {len(nomes[0])} letras')


