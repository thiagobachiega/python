largura = float(input('Qual a largura da parede?:'))
altura = float(input('Qual a altura da parede?:'))

area = largura * altura
tinta = area /2

print('Sua parede tem uma area de:{}M e precisa de {:.2f}L de tinta'.format(area, tinta))


