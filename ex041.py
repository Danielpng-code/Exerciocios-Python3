from datetime import date

nascimento = int(input('Digite aqui ano de nascimento do atleta: '))
nome = str(input('Digite o nome do atleta: '))
idade = date.today().year - nascimento
print(idade)

if idade <= 9:
    print('Esse atleta de nome {}, tem {} anos e ira participar na categoria de natação mirim'.format(nome, idade))

elif idade > 9 and idade <= 14:
    print('Esse atleta de nome {}, tem {} anos e ira participar na categoria de natação infantil'.format(nome, idade))

elif idade > 14 and idade <= 19:
    print('Esse atleta de nome {}, tem {} anos e ira participar na categoria de natação junior'.format(nome, idade))

elif idade > 19 and idade <=20:
    print('Esse atleta de nome {}, tem {} e ira participar na categoria de natação senior'.format(nome, idade))

else:
    print('Esse atleta de nome {}, tem {} anos e ira participar na categoria de natação master'.format(nome, idade))
