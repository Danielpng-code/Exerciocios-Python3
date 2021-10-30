num1 = int(input('Digite aqui o primeiro numero: '))
num2 = int(input('Digite aqui o segundo numero: '))
num3 = int(input('Digite aqui o terceiro numero: '))

## Verificando quem e menor ##

if num1 < num2 and num1 < num3:
    print('O numero {} e o menor'.format(num1))

if num2 < num3 and num2 < num1:
    print('O numero {} e o menor'.format(num2))

if num3 < num1 and num3 < num2:
    print('O numero {} e o menor'.format(num3))

## Verificando quem e maior ##

if num1 > num2 and num1 > num3:
    print('O numero maior e o numero {}'.format(num1))

if num2 > num1 and num2 > num3:
    print('O numero maior e o numero {}'.format(num2))

if num3 > num1 and num3 > num2:
    print('O numero maior e o numero {}'.format(num3))

######## outra maneira de resolver ########

## Verificando quem e menor ##

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O numero {} e o menor'.format(menor))

## Verificando quem e maior ##

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O numero {} e o maior'.format(maior))
