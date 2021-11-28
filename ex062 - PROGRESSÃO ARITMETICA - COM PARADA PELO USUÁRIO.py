print('Gerador de P.A')
print('-=' * 10)
primeiro = int(input('Digite aqui o primeiro termo: '))
razao = int(input('Digite aqui a razão: '))
resultado = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais

    while contador <= total:
        print('{} - '.format(resultado), end='')
        resultado = resultado + razao
        contador = contador + 1
    print(('Pausa'), end=' ')
    print('\nValor do resultado', resultado)
    mais = int(input('Quantos termos você quer mostrar a mais agora ? '))


print('!!!!!!!!!Acabamos, a progressão mostrou {} termos ate o final!!!!!!!!!!'.format(total))
