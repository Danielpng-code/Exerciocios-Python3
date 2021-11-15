soma = 0
cont = 0

for contador in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(contador)))

    if numero % 2 == 0:
        soma = soma + numero
        cont = cont + 1

print('Voce digitou {} numeros pares, e a soma deles e de {}'.format(cont, soma))








