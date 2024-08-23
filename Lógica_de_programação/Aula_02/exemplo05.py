numeros = [3, 1, 6]

n1 = 3
n2 = 1
n3 = 6

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

meio = n1

if n2 > menor and n2 < maior:
    meio = n2
if n3 > menor and n3 < maior:
    meio = n3

print(menor, meio, maior)
print(maior, meio, menor)
#-------------------------------------
print(sorted(numeros))
print(sorted(numeros, reverse=True))


