total18 = 0
totalhomens = 0
totalmulheres20 = 0
totalmulheresmais20 = 0
totalhomensmaisde30 = 0

while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalhomens += 1

    if sexo == 'F' and idade < 20:
        totalmulheres20 += 1

    if sexo == 'F' and idade > 20:
        totalmulheresmais20 += 1

    if sexo == 'M' and idade > 30:
        totalhomensmaisde30 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'Pessoas com mais de de 18 anos, total de {total18}')
print(f'Ao todos temos {totalhomens} homens cadastrados')
print(f'Ao total temos {totalmulheres20} mulheres com menos de 20 anos')
print(f'No total temos {totalmulheresmais20} mulheres com mais de 20 anos')
print(f'No total temos {totalhomensmaisde30} homens com mais de 30 anos')


