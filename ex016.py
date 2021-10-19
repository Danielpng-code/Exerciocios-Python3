import math
num = float(input('Digite qualquer numero: '))
print('O numero {} tem a parte inteira {:.0f}'.format(num, math.floor(num)))

print('O numero {} tem a parte inteira {:.0f}'.format(num, math.trunc(num)))

print('O numero {} tem a parte inteira {:.0f}'.format(num, int(num)))

