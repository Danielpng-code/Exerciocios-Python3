import random

escolha = int(input('Digite aqui sua escolha \n [ 1 ] - Pedra \n [ 2 ] - Papel \n [ 3 ] - Tesoura: '))

escolhaPessoa1 = 'Pedra'
escolhaPessoa2 = 'Papel'
escolhaPessoa3 = 'Tesoura'

escolhapc = random.randint(1, 3)

escolhapc1 = 'Pedra'
escolhapc2 = 'Papel'
escolhapc3 = 'Tesoura'

print('A escolha do PC foi {}'.format(escolhapc))

if escolha == 1 and escolhapc == 1:
   print('\n Tivemos um empate - {} não ganha de {}'.format(escolhaPessoa1, escolhapc1))

elif escolha == 1 and escolhapc == 2:
    print('\n O PC ganhou - {} não ganha de {}'.format(escolhaPessoa1, escolhapc2))

elif escolha == 1 and escolhapc == 3:
    print('\n Você ganhou - {} ganha de {}'.format(escolhaPessoa1, escolhapc3))

elif escolha == 2 and escolhapc == 1:
    print('\n Você ganhou - {} ganha de {}'.format(escolhaPessoa2, escolhapc1))

elif escolha == 2 and escolhapc == 2:
    print('\n Tivemos um empate - {} não ganha de {}'.format(escolhaPessoa2, escolhapc2))

elif escolha == 2 and escolhapc == 3:
    print('\n O PC ganhou - {} não ganha de {}'.format(escolhaPessoa2, escolhapc3))

elif escolha == 3 and escolhapc == 1:
    print('\n O PC ganhou - {} não ganha de {}'.format(escolhaPessoa3, escolhapc1))

elif escolha == 3 and escolhapc ==2:
    print('Você ganhou - {} ganha de {}'.format(escolhaPessoa3, escolhapc2))

elif escolha == 3 and escolhapc == 3:
    print('Tivemos um empate - {} ganha de {}'.format(escolhaPessoa3, escolhapc3))

else:
    print('Escolha uma opção válida')
