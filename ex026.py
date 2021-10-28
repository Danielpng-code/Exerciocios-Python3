frase = str(input('Escreva uma frase qualquer: ')).upper().strip()

print('A letra "A" aparece {} vezes: '.format(frase.count('A')))


print('A letra "A" aparece a primeira vez na posição: {} '.format(frase.find('A')+1))


print('A letra "A" aparece a ultima vez na posição: {} '.format(frase.rfind('A')+1))

