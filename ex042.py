reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))


if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Podemos montar um triangulo com essas medidas!!!')

    if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print('As medidas de {} + {} + {} formam um triangulo Equilátero !!!'.format(reta1, reta2, reta3))

    elif reta1 == reta2 and reta2 != reta3 or reta2 == reta3 and reta3 != reta1 or reta3 == reta1 and reta2 != reta1:
        print('As medidas de {} + {} + {} formam um triangulo Isóceles !!!'.format(reta1, reta2, reta3))

    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('As medidas de {} + {} + {} formam um triangulo Escaleno !!!'.format(reta1, reta2, reta3))

else:
    print('Os valores {} + {} +{} não podem formar um triangulo'.format(reta1, reta2, reta3))
