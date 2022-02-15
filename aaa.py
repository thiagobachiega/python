arquivo = link = 0

arquivo = int(input('Informe o tamanho do arquivo[MB]: '))
link = int(input('Informe a velocidade do link de internet[MB]'))

tempo = (arquivo / link) / 60

print(f'Para baixar um arquivo de {arquivo} MB com um link de {link} MB vai levar em média {tempo:.0f} minutos e {arquivo / link:.0f} segundos')
