import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COS de {:.2f}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TAN de {:.2f}'.format(angulo, tan))


