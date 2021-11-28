#Minha Resolução

primeiro = int(input('Digite aqui o primeiro termo: '))
razao = int(input('Digite aqui a razão: '))
contador = primeiro
decimotermo = primeiro + 10 * razao


while contador != decimotermo:
    print('{}'.format(contador), end=' ')
    contador = contador + razao

print('Acabamos!!!!')

#Resolução do Guanabara

print('\nGerador de P.A')
print('-=' * 10)
primeiro1 = int(input('Digite aqui o primeiro termo: '))
razao1 = int(input('Digite aqui a razão: '))
termo = primeiro1
contador1 = 1
while contador1 <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razao1
    contador1 = contador1 + 1
print('!!!!!!!!!Acabamos!!!!!!!!!!')
