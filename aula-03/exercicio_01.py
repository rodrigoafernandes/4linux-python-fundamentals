numeros = [5,10,22,45,30,92,88,34,55]
pares = []
impares = []
soma_total = 0
soma_pares = 0
soma_impares = 0
indice = 0

for num in numeros:
    soma_total += num
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

    if indice % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    indice += 1

print('Os elementos são: {}'.format(numeros))
print('A soma de todos os elementos é: {}'.format(soma_total))
print('A soma dos elementos pares é: {}'.format(soma_pares))
print('A soma dos elementos impares é: {}'.format(soma_impares))
print('A quantidade de elementos é: {}'.format(len(numeros)))
print('Os elementos de indice par são: {}'.format(pares))
print('Os elementos de indice impar são: {}'.format(impares))
