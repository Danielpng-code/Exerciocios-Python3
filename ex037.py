import math

numero = int(input('Digite qualquer numero inteiro aqui: '))
escolha = int(input('\n Digite aqui qual a sua escolha de conversão, \n [ 1 ]- Binário \n [ 2 [- Octal \n [ 3 ]- Hexadecimal \n Sua Opção: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

if escolha == 1:
    print('O numero {}, convertido para Binário e {}'.format(numero, binario))

elif escolha == 2:
    print('O numero {}, convertido para Octal e {}'.format(numero, octal))

elif escolha == 3:
    print('O numero {}, convertido para Hexadecimal e {}'.format(numero, hexadecimal))

else:
    print('Essa não e uma opção válida!!!, digite um valor entre as opções!!!')
