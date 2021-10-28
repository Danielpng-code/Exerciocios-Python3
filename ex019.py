import random

alu1 = str(input ('Escreva o nome do primeiro aluno: '))
alu2 = str(input ('Escreva o nome do segundo aluno: '))
alu3 = str(input ('Escreva o nome do terceiro aluno: '))
alu4 = str(input ('Escreva o nome do quarto aluno: '))

sorteio = random.randint(1, 4)

print('O resultado do sorteio foi o numero: {}' .format(sorteio))
if sorteio == 1:
    print('O aluno sorteado foi o : {}' .format(alu1))
if sorteio == 2:
    print('O aluno sorteado foi o : {}' .format(alu2))
if sorteio == 3:
    print('O aluno sorteado foi o : {}' .format(alu3))
if sorteio == 4:
    print('O aluno sorteado foi o : {}' .format(alu4))

# -------------------------------------------------------------------------- #

alu1 = str(input('Escreva o nome do primeiro aluno: '))
alu2 = str(input('Escreva o nome do segundo aluno: '))
alu3 = str(input('Escreva o nome do terceiro aluno: '))
alu4 = str(input('Escreva o nome do quarto aluno: '))

lista = [alu1, alu2, alu3, alu4]

escolhido = random.choice(lista)

print('o Aluno escolhido foi {}'. format(escolhido))
