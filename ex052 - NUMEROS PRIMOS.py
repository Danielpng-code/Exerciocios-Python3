numero = int(input('Digite um numero para saber se ele e primo ou não: '))
total = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('\n\033[mO numero {} foi dividido {} vezes'.format(numero, total))
if total == 2:
    print('Por isso ele e um número primo!!!')
else:
    print('E por isso ele não e um número primo!!!!')


