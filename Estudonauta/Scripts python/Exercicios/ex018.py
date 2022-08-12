'''from math import sin, cos, tan, radians'''
import math
angulo = float(input('Digite o angulo que vc deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COS de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a TAN de {:.2f}'.format(angulo, tangente))
