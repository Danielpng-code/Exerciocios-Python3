valorcasa = float(input('Digite o valor da casa que quer comprar R$ '))
salario = float(input('Digite aqui o valor do seu sálario bruto R$ '))
tempo = int(input('Digite em quantos anos vai pagar a casa: '))

tempo = tempo * 12
print('\n Financiamento em {} meses'.format(tempo))

parcela = valorcasa / tempo
print('\n O valor de parcela que irá pagar e de R${:.2f}'.format(parcela))

parcelapessoa = salario * 0.3
print('\n Você pode pagar ate R${} de parcela mensal'.format(parcelapessoa))


if parcela <= salario * 0.3:
    print('\n O valor R${:.2f} esta aprovado no financiamento!!!'.format(parcela))

else:
    print('\n Infelizmente não foi aprovado seu financiamento, parcela ficará em R${:.2f}, e você so pode pagar R${:.2f}'.format(parcela, parcelapessoa))
