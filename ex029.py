velocidade = int(input('Digite aqui a velocidade que você estava: '))

if velocidade <= 80:
    print('Você não foi multado, pode rodar tranquilo {} Km/h, não da multa: '.format(velocidade))


else:
    multa = (velocidade - 80) * 7
    print('Você foi multado e tera de pagar uma multa de R${:.2f} '.format(multa))

