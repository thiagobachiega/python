r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
   print('Podem formar um triangulo')
   if r1 == r2 and r2 == r3 and r1 == r3: #pode ser feito também com: 'if r1 == r2 == r3:', sem utilizar a função AND
       print('Equilátero')
   elif r1 == r2 or r1 == r3 or r2 == r3:
       print('Isósceles')
   elif r1 != r2 and r1 != r3 and r2 != r3:
       print('Todos os lados são diferentes')
else:
    print('Não podem formar um triangulo!')
