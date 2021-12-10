from random import randint
vitoria = 0
while True:
   jogador = int(input('Escolha um numero para jogar par ou impar: '))
   computador = randint(0, 10)
   total = jogador + computador
   escolha = ' '

   while escolha not in 'PI':
        escolha = str(input('Par ou Impar ? [P/I] ')).strip().upper()[0]
   print(f'Você jogou {jogador}, e o PC {computador}, temos um total de {total}')
   print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

   if escolha == 'P':
       if total % 2 == 0:
           print('Você venceu!!!!')
           vitoria += 1
       else:
           print('Você perdeu infelizmente')
           break

   elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu!!!!!')
            vitoria += 1
        else:
            print('Você perdeu infelizmente')
            break

   print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')



