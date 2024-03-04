n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3    

print(f"O número maior é {maior}")

