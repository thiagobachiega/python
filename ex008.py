m = float(input('Qual a distancia em metros?'))
km = float(m /1000)
cm = float(m *100)
mm = float(cm *100)

print('Uma medida de {} corresponde a:'.format(m))
print('{}Km \n{:.0f}cm \n{:.0f}mm'.format(km, cm, mm))