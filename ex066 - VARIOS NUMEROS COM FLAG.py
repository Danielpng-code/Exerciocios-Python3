soma = 0
quantidade = 0
while True:
    numero = int(input('Digite um valor: [Digite 999 para parar]'))
    if numero == 999:
        break
    quantidade = quantidade + 1
    soma = soma + numero



print(f'Foram digitados {quantidade} numeros, e a soma dos valores e de {soma}')

#Para fixação

#contador += 1
#soma += numero