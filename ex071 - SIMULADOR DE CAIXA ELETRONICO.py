print('=' * 30)
print('{:^30}'.format('BANCO DGA'))
print('=' * 30)
valorsaque = int(input('Qual valor desejas sacar ?R$'))
totaldinheiro = valorsaque
cedula = 100
totalcedula = 0
while True:
    if totaldinheiro >= cedula:
        totaldinheiro -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(F'Total de {totalcedula} cedulas de R$ {cedula}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalcedula = 0
        if totaldinheiro == 0:
            break

print('=' * 30)
print('Volte sempre em nosso banco!!!')
