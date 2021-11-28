#Minha resolução do problema

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

print()

escolha = 0

while escolha == 0 and 1 and 2 and 3 and 4 and 5:

    escolha = int(input('Digite qual operação deseja fazer: \nDigite [1] Para Somar: \nDigite [2] Para multiplicar: \nDigite [3] Para maior valor: \nDigite [4] Para inserir novos numeros: \nDigite [5] Para Sair: '))

    if escolha == 1:
        soma = numero1 + numero2
        print(soma)

    if escolha == 2:
        multiplicacao = numero1 * numero2
        print(multiplicacao)

    if escolha == 3:
        if numero1 > numero2:
            print('o numero {} e maior que o numero {}'.format(numero1, numero2))
        else:
            print('o numero {} e maior que o numero {}'.format(numero2, numero1))

if escolha == 4:
    print('Você deseja inserir novos números!!')
    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))

escolha = 0
while escolha == 0 and 1 and 2 and 3 and 4 and 5:

    escolha = int(input('Digite qual operação deseja fazer: \nDigite [1] Para Somar: \nDigite [2] Para multiplicar: \nDigite [3] Para maior valor: \nDigite [4] Para inserir novos numeros: \nDigite [5] Para Sair: '))

    if escolha == 1:
        soma = numero1 + numero2
        print(soma)

    if escolha == 2:
        multiplicacao = numero1 * numero2
        print(multiplicacao)

    if escolha == 3:
        if numero1 > numero2:
            print('o numero {} e maior que o numero {}'.format(numero1, numero2))
        else:
            print('o numero {} e maior que o numero {}'.format(numero2, numero1))

    if escolha == 5:
        print('Fim das operações: Saindo')

print('-----FIM-----')


#Solução do Guanabara

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [ 1 ] Somar 
    [ 2 ] Multiplicação
    [ 3 ] Mostrar o maior numero 
    [ 4 ] Digitar novos numeros 
    [ 5 ] Sair do programa ''')
    opcao = int(input('Qual e a sua escolha: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} e de {}'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicacao1 = n1 * n2
        print('A multiplicação entre {} x {} e de {}'.format(n1, n2, multiplicacao1))

    elif opcao == 3:
        if n1 > n2:
            print('O numero {} e maior que o numero {}'.format(n1, n2))
        if n2 > n1:
            print('O numero {} e maior que o numero {}'.format(n2, n1))
        if n1 == n2:
            print('O numero {} e igual ao numero {}'.format(n1, n2))

    elif opcao == 4:
        print('Informe os novos numeros que deseja fazer as operações: ')
        n1 = int(input('Digite o valor do novo primeiro numero: '))
        n2 = int(input('Digite o valor do novo segundo numero: '))
    elif opcao == 5:
        print('Finalizando o programa!!!!')

    else:
        print('Digite uma opção válida, tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!!')


