larg = float(input('Digite a medida da largura da parede: '))
altura = float(input('Digite a medida da altura da parede: '))
area = float(larg * altura)
print('Sua parede mede {:.4f}m²'.format(area))

rendimento = float(area/2)

print('Vamos gastar {:.4f}'.format(rendimento), 'litros de tintas para pintar essa parede')
