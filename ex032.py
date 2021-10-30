import datetime

ano = int(input('Digite aqui o ano que deseja saber se e bissexto ou não. coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} e um ano Bissexto'.format(ano))
else:
    print('Esse ano {} não e bissexto, foi mal'.format(ano))


