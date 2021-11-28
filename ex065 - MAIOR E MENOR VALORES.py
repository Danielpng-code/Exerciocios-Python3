#-----------------------------------------------------------------Minha Resolução---------------------------------------------------------------------------#
continuar = 'S'
soma = 0
quantidade = 0
maior = 0
menor = 0
media = 0

while continuar in 'Ss':
    numero = int(input('Digite um valor qualquer: '))
    soma = soma + numero
    quantidade = quantidade + 1

    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
    continuar = str(input('Você deseja continuar com as operações?: [S/N]')).upper().strip()[0]
media = soma / quantidade
print('!!!!!!Acabamos, foi digitado {} numeros e a media entre eles e de {}, o maior numero digitado foi {} e o menor numero {} !!!!!!'.format(quantidade, media, maior, menor))


#------------------------------------------------------------------------Resolução Guanabara-------------------------------------------------------------------#

resposta = 'S'
soma1 = quantidade1 = media1 = maior1 = menor1 = 0
while resposta in 'Ss':
    numero1 = int(input('Digite um numero: '))
    soma1 = soma1 + numero1
    #soma += num
    quantidade1 = quantidade1 + 1
    #quantidade += 1

    if quantidade1 == 1:
        maior1 = menor1 = numero1
    else:
        if numero1 > maior1:
            maior1 = numero1

        if numero1 < menor1:
            menor1 = numero1

    resposta = str(input('Quer continuar: [S/N] ')).upper().strip()[0]

media1 = soma1 / quantidade1

print('!!!!Voce digitou {} numeros e a media e de {} !!!!'.format(quantidade1, media1))
print('O maior numero foi {}, e o menor numero {}'.format(maior1, menor1))
