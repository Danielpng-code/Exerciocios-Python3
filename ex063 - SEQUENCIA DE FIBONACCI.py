print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'* 30)

numtermos = int(input('Quando termos da sequencia de fibonacci você deseja ver ? '))
termo1 = 0
termo2 = 1
print('~' * 30)
print('{}  - {}'.format(termo1, termo2), end='')
contador = 3
while contador <= numtermos:
    termo3 = termo1 + termo2
    print(' - {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1
print(' - ACABAMOS!!!')
