somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totalmulhere20 = 0

for pessoa in range(1, 5):
    print('---------- {}ª Pessoas ---------'.format(pessoa))
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip()

    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome

    if sexo in 'Ff' and idade < 20:
         totalmulhere20 = totalmulhere20 + 1

mediaidade = somaidade / 4

print('\nA media de idade e de {} anos!!!!'.format(mediaidade))
print('\nO nome do homem mais velho e {} e ele te {} anos!!!'.format(nomemaisvelho, maioridadehomem))
print('\nAo todo são {} mulher(es) com menos de 20 anos!!!!'.format(totalmulhere20))
