peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui a sua altura: '))

IMC = peso / (altura * altura)
print('\n Seu IMC e de {:.2f}'.format(IMC))

if IMC < 18.5:
    print('\n Seu IMC e de {:.2f}, e você está abaixo do peso ideial!!!!'.format(IMC))

elif IMC >= 18.5 and IMC < 25:
    print('\n Seu IMC e de {:.2f}, e você está no peso ideial!!!! Parabéns !!!!'.format(IMC))

elif IMC >= 25 and IMC < 30:
    print('\n Seu IMC e de {:.2f}, e você esta com sobrepeso, vamos treinar em!!!!'.format(IMC))

elif IMC >= 30 and IMC <40:
    print('\n Seu IMC e de {:.2f}, e você esta com obesidade, vamos treinar e fazer dieta!!!'.format(IMC))

elif IMC > 40:
    print('\n Seu IMC e de {:.2f}, e você esta com obesidade morbida, vamos treinar, fazer dieta e acompanhamento com médico especializado'.format(IMC))
