import math
angulo = float(input('Digite o valor do angulo aqui: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('A medida e do Seno e de {:.2f}, a medida do consseno e de {:.2f}, a medida da tangente e de {:.2f}'. format(seno, cosseno, tangente))
