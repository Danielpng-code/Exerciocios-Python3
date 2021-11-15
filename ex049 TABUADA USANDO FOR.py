tabuada = int(input("Digite um valor para saber sua tabuada: "))
cont = 0
resultado = int

for contador in range(0, 11):
     resultado = tabuada * cont
     print('{} x {} = {}'.format(tabuada, cont, resultado))
     cont += 1

tabuada2 = int(input('Digite um numero para saber sua tabuada: '))

for contador2 in range(0, 11):
     print('{} x {} = {}'.format(contador2, tabuada2, contador2 * tabuada2))
