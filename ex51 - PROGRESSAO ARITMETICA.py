primeiro = int(input('Digite aqui o primeiro termo: '))
razao = int(input('Digite aqui a razão: '))
decimotermo = primeiro + (10) * razao
for contador in range(primeiro, decimotermo, razao):
    print('{}'.format(contador), end='- ')
print('Acabamos!!!!')


