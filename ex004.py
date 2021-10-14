algo = input('Digite algo do teclado: ')
print('O tipo primitivo desse valor e: ', type(algo))

print('Esse dado e alfanumerico ?', algo.isalnum())
print('Esse dado esta em caixa baixa ?', algo.islower())
print('Esse dado esta em caixa alta ?', algo.isupper())
print('Esse dado e alfabetico? ', algo.isalpha())
print('Esse dado e um numero ?', algo.isnumeric())
print('Esse dado e um digito decimal? ', algo.isdigit())
print('Esse dado esta capitalizado? ', algo.istitle())

#capitalizado quer dizer que ele tem letras em maiusculo e minusculo
