preco = float(input('Digite aqui o valor do produto: R$'))
escolha = int(input('Qual vai ser o meio de pagamento \n [ 1 ] - A vista Dinheiro/Cheque \n [ 2 ] - Cartão a vista \n [ 3 ] - Duas vezes no cartão \n [ 4 ]- 3 vezes ou mais no cartão: '))

avista = preco - (preco * 0.1)
avistacartao = preco - (preco * 0.05)
duasxcartao = preco
tresxcartao = preco + (preco * 0.2)

if escolha == 1:
    print('\n O valor a ser pago e de R${}'.format(avista))

elif escolha == 2:
    print('\n O valor a ser pago e de R${}'.format(avistacartao))

elif escolha == 3:
    parcela = preco / 2
    print('\n O valor total a ser pago e de R${}, e suas parcelas vão ser de R${}, sem juros'.format(duasxcartao, parcela))

elif escolha == 4:
    totalparcelas = int(input('Quantas parcelas vai dividir ? '))
    parcela = ((preco * 0.2) + preco) / totalparcelas
    print('\n O valor total a ser pago e de R${}, e suas parcelas vão ser de {} x R${}'.format(tresxcartao, totalparcelas, parcela))

else:
    preco == 0
    print('\n Opção de pagamaneto invalida!!!!, \n Tente novamente e escolha uma opção válida')




