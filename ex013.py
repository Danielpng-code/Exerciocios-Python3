salarioatual = float(input('Digite aqui o salario atual do funcionário: R$ '))
aumento = salarioatual * 0.15
novosalario = salarioatual + aumento

print('O salario atual do funcionário e de R${:.3f} reais, e com o aumento o novo salario do vai ser de R${:.3f} reais'.format(salarioatual,novosalario))
