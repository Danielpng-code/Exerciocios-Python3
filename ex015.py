dias = int(input('Quantos dias o carro ficou alugado ? '))
kmRodado = float(input('Quantos kms o veiculo rodou ? '))

valor = (dias * 60) + (kmRodado * 0.15)

dias = dias * 60
kmRodado = kmRodado * 0.15

print('O valor total da locação do veículo e de R${:.2f}, desse valor R${:.2f} são referentes aos dias de locação e R${:.2f} são referentes aos KMs rodados' .format(valor, dias, kmRodado))