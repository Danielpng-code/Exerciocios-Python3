while True:
    numero = int(input('Digite um valor para ver sua tabuada: [para sair do programa digite qualquer numero negativo]'))
    if numero < 0:
        break
    print('-=' * 30)
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero * contador}')
    print('-=' * 30)
print('-=' * 30)
print('Tabuada encerrada')
print('-=' * 30)










