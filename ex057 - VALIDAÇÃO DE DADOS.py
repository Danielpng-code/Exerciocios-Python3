#Minha Resolução
sexo = str
resposta = str

while resposta != 'N':
    sexo = str(input('Digite seu sexo aqui: ')).upper()

    if sexo != 'F' and 'M':
        print('Digite uma opção válida!!!')

    else:
        print('Opção valida digitada!!!')

    resposta = str(input('Deseja continuar? S/N: ')).upper()

print('!!!!!!!Fimmmm!!!')


#Resolução Guanabara

sexo1 = str(input('Informe aqui seu sexo: [M/F]')).strip().upper()[0]

while sexo1 not in 'MF':
    sexo1 = str(input('Dados inválidos: Por favor informar os dados válidos: [F/M]')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo1))

#O que aprendemos com esse exercio, não me recordava que ele tinha passado sobre o whlie not in, fica bem mais fácil de fazer assim, visto que temos uma condição diferente do que eu tinha feito, meio que fica ao contrário da condição que eu usei

