zeros = 0
numero = 0
while (numero <= 0):
    numero = int(input("Verificar se o número é primo: "))
    if (numero <= 0):
        print("O numero deve ser positivo!")

for i in range(2, numero+1):
    if (numero % i == 0):
        zeros += 1

print(f"O número {numero} é primo" if zeros == 2 else f"O número {numero} não é primo")