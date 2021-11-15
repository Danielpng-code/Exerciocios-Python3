frase = str(input('Digite uma frase para sabe se ele e um Palindromo: ')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
print(junto)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('a frase digitada foi {}, essa frase sem espaços fica assim {} e o inverso dessa frase e {}'.format(frase, junto, inverso))
if inverso == junto:
    print('Por isso temos uma frase palindroma')
else:
    print('E por isso não temos uma frase palindroma')

