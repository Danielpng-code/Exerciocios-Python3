salario = float(input('Digite o valor do salario do funcionário hoje: '))

if salario <= 1250:
    salario15 = salario + (salario * 0.15)
    print('O novo salario vai ser de R${:.2f}'.format(salario15))

else:
    salario10 = salario + (salario * 0.10)
    print('O novo salario vai ser de R${:.2f}'.format(salario10))
