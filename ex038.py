num1 = int(input('Digite aqui o primeiro valor: '))
num2 = int(input('Digite aqui o segundo valor: '))

if num1 > num2:
    print('O numero {} e maior que o numero {}, o primeiro valor digitado e maior'.format(num1, num2))

elif num2 > num1:
    print('O numero {} e maior que o numero {},  o segundo valor digitado e maior'.format(num2, num1))

else:
    print('{} e {} são valores iguais'.format(num1, num2))


