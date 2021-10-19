import random

alu1 = str(input('Escreva o nome do primeiro aluno: '))
alu2 = str(input('Escreva o nome do segundo aluno: '))
alu3 = str(input('Escreva o nome do terceiro aluno: '))
alu4 = str(input('Escreva o nome do quarto aluno: '))

lista = [alu1, alu2, alu3, alu4]

random.shuffle(lista)

print('A ordem de apresentação será: {} '.format(lista))