nome = str(input('Digite seu nome completo aqui: ')).strip()

print('Seu nome com as letras maiusculas e {}.'.format(nome.upper()))

print('Seu nome com as letras minusculas e {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'. format(len(nome)-nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()

print('Seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))





