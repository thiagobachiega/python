a = input('Digite algo:')

print('Tipo:{}, Alfanumérico?:{}, Caracter e?:{}, Minusculo:{}, Maisculo:{}'.format(type(a), a.isalnum(), a.isalpha(), a.islower(), a.isupper()))
