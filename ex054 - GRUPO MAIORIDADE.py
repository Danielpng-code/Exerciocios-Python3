from datetime import date

anoatual = date.today().year
totalmaioridade = 0
totalmenoridade = 0

for pessoas in range(1, 7, 1):
    nascimento = int(input('Digite o ano de {}º nascimento da pessoa aqui: '.format(pessoas)))
    idade = anoatual - nascimento

    print('Sua idade e de {} anos'.format(idade))

    if idade < 18:
       totalmaioridade = totalmaioridade + 1

    elif idade >= 18:
        totalmenoridade = totalmenoridade + 1

print('O total de pessoas com menoridade e de {}'. format(totalmenoridade))
print('O total de pessoas com maioridade e de {}'.format(totalmaioridade))


