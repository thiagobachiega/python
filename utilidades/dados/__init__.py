def cdin(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO VALOR INVALIDO!')
        else:
            valido = True
            return float(entrada)