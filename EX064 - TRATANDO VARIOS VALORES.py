#----------------------------------------------------Minha Solução------------------------------------------------------------#

#essa parte também pode ser feia assim "numero = contador = soma = 0", vamos deixar assim para podermos fixar o exercicio
numero = 0
contador = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um valor para saber sua soma [999 para as operações]: '))
    soma = soma + numero
    #soma pode ser demonstrato assim tbm soma += numero
    contador = contador + 1
    #contador pode ser demonstrato assim tbm contado += 1
    if numero == 999:
        soma = soma - 999

contador = contador - 1
print('!!!!!Acabamos, foi digitado {} numeros,e a soma entre eles e de {} !!!!!'.format(contador, soma))

#-----------------------------------------------------Solução Guanabara----------------------------------------------------#

numero1 = contador1 = soma1 = 0
numero1 = int(input('Digite um valor para saber sua soma [999 para as operações]: '))

while numero1 != 999:
    soma1 += numero1
    contador1 += 1
    numero1 = int(input('Digite um valor para saber sua soma [999 para as operações]: '))

print('!!!!!Acabamos, foi digitado {} numeros,e a soma entre eles e de {} !!!!!'.format(contador1, soma1))
