precoprod = float(input('Digite aqui o preço do produto sem desconto: R$ '))
desconto = (precoprod * 0.05)
precocomdesconto = precoprod - desconto



print('O valor do produto com desconto e de R${:.2f} reais \n'.format(precocomdesconto))

if desconto < 1.0:
    print('Você ganhou R${:.2f} centavos de desconto'.format(desconto))
else:
    print('Você ganhou R${:.2f} reais de desconto'.format(desconto))
