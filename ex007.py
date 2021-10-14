nome = input('Qual nome do aluno? ')
nota1 = float(input('Escreva a primeira nota do aluno: '))
nota2 = float(input('Escreva a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('A media do aluno',nome,'e de {} pontos'.format(media))