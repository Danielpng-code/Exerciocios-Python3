from datetime import date

nascimento = int(input('Digite o ano que você nasceu aqui: '))
sexo = str(input('Qual e seu sexo de nascimento ? ')).upper()

if sexo == 'FEMININO':
    print('Você não e obrigada a fazer o alistamento militar!!!!')

elif sexo == 'MASCULINO':

    hoje = date.today().year
    print(hoje)

    idade = hoje - nascimento
    print(idade)

    alistamento = nascimento + 18
    print(alistamento)


    if idade == 18:
        print('Voê tem {} anos e deve ser alistar imediatamente!!!!'.format(idade))

    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para você se alistar!!!'.format(saldo))
        print('Você ainda não precisa se alistar, você tem {} anos e deve ser alistar em {}'.format(idade, alistamento))

    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado a {} anos!!!!'.format(saldo))
        print('Você ja deveria ter se alistado no serviço militar em {}'.format(alistamento))
