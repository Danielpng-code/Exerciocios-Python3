import random

escolha = int(input('Digite um valor de 1 a 5 que você achar que sera sorteado: '))

numero = random.randint(0, 5)

print(numero)

if numero == escolha:
    print('Você escolheu o numero e {} e ganhou o desafio, parabens!!!! '.format(escolha))
else:
    print('Infelizmente você errou o numero, o numero sorteado foi {}'.format(numero))
