tabuada = int(input("Digite um valor para saber sua tabuada: "))
cont = 0
num = tabuada
result = int

while (cont <= 10):
     result = num * cont
     print(tabuada, 'x', cont, '= {}'.format(result))
     cont += 1
