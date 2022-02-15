sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = input('Informe o sexo do paciente [M/F]').upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor invalido, tente novamente!')