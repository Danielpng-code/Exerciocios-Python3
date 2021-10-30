distancia = float(input('Digite quantos kms tera a viagem: '))

if distancia <= 200:
    preco1 = distancia * 0.50
    print('Sua passagem irá custa R${:.2f}'.format(preco1))

else:
    preco2 = distancia * 0.45
    print('Sua passagem vai custar R${:.2f}'.format(preco2))


