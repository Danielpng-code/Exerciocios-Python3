import math

catopos = float(input('Digite o valor da medida do Cateto Oposto: '))
catadj = float(input('Digite o valor da medida do Cate Adjacente: '))

hipot = math.hypot(catopos, catadj)

"hipot = (catopos ** 2 + catadj ** 2) **(1/2)"

print('O valor valor da  Hipotenusa e :{:.2f}'.format(hipot))
