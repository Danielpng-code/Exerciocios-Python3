nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nome = str(input('Digite o nome do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Aluno {}, tirou nota de {} pontos e foi reprovado'.format(nome, media))

elif media >= 5 and media < 6.9:
    print('Aluno {} tirou nota de {} pontos e esta de recuperação'.format(nome, media))

elif media >= 7:
    print('Aluno {} tirou nota de {} pontos e foi aprovado na materia'.format(nome, media))

