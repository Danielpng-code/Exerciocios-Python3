#Minha resolução

contador = int(input('Digite um valor para saber seu fatorial: '))
print(contador)

fatorial = contador
print(fatorial)

acumulado = fatorial
print(acumulado)

while contador > 0:

    resultado = acumulado * (contador - 1)
    contador = contador - 1
    acumulado = resultado

    print('O resultado fatorial do numero {} e igual a {}'.format(fatorial, acumulado))

print(contador)


#Resolução Guanabara
#Modo resumido

from math import factorial
from time import sleep

numero = int(input('Digite um valor para saber seu fatorial: '))
fatorial1 = factorial(numero)
print('O fatorial do numero {} e {}'.format(numero, fatorial1))

#Modo classico

numero1 = int(input('Digite um valor para saber seu fatorial: '))
contador1 = numero1
fatorial2 = 1
print('Calculando {}! = '.format(numero1), end='')

while contador1 > 0:
    print('{}'.format(contador1), end=' ')
    print('x' if contador1 > 1 else ' = ', end=' ')
    fatorial2 = fatorial2 * contador1
    contador1 = contador1 - 1

sleep(1)
print('O fatorial de {} e {}'.format(numero1, fatorial2))

# O que aprendemos sobre esse exercicio foi, temos uma biblioteca de matematica ja para uso com fatorial, sabiamos da biblioteca, porém não dessa extensão, aprendetemos o uso do cotador - para as multiplicações.