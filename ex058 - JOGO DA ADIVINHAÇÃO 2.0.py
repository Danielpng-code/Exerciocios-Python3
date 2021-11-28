#Minha resolução do exercicio

import random

numero = random.randint(1, 11)

print(numero)

contador = 1
escolha = int

while escolha != numero:

    escolha = int(input('Digite um valor de 1 a 10 que você achar que sera sorteado: '))

    if escolha != numero:
        print('Você não escolheu o numero correto!!!! ')
        contador = contador + 1

    if escolha == numero:
        print('Você gastou {} tentativas para acertar o numero '.format(contador))

print('------------Acabou------------')

#Resolução do Guanabara

from random import randint

computador = randint(0, 10)
print(computador)
print('Eu sou seu computador, e vou pensar em um numero, entre 0 e 10')
print('Tente adivinhar qual numero eu pensei por favor')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual numero e seu palpite: '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O numero que você escolhe e menor, tente de novo...')
        elif jogador > computador:
            print('O numero que você escolhe e maior, tente de novo...')


print('\nAcertou Miseravi!!!!! você acertou com {} tentativas !!!!'.format(palpites))

# o que aprendemos desse exercicio foi, o uso do while not, que não foi repassado na aula antes, e também foi bom lembrar que da pra usar un IF dentro de um else para faze as condições

