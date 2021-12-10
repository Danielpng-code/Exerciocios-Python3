totalcompra = 0
totalmaisde1000 = 0
menorpreco = 0
contador = 0
barato = ' '

while True:
    nomeproduto = str(input('Digite o nome do produto que desejas comprar: '))
    precoproduto = float(input('Digite aqui o valor do produto que deseja comprar: R$ '))
    contador += 1
    totalcompra = totalcompra + precoproduto

    if precoproduto > 1000:
        totalmaisde1000 += 1

    if contador == 1 or precoproduto < menorpreco:
        menorpreco = precoproduto
        barato = nomeproduto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Desejas continuar : ')).strip().upper()[0]
    if resposta == 'N':
        break

print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {totalcompra:.2f}')
print(f'A quantidade de produtos com valor acima de mil reais e de {totalmaisde1000} produtos')
print(f'O produto mais barato foi {barato} custa R$ {menorpreco:.2f}')

