maiorpeso = 0
menorpeso = 0

for pesopessoa in range(1, 6, 1):
    peso = float(input('Digite aqui o peso da {}ª pessoa: '.format(pesopessoa)))

    if pesopessoa == 1:
        maiorpeso = peso
        menorpeso = peso

    else:
        if peso < menorpeso:
            menorpeso = peso

        if peso > maiorpeso:
            maiorpeso = peso

print('\nO maior peso da lista e de {}kg'.format(maiorpeso))
print('O menor peso da lista e de {}kg'.format(menorpeso))



