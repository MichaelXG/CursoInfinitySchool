
numero = 0
while (numero <= 0):
    numero = int(input("Verificar se o número é primo: "))
    if (numero <= 0):
        print("O numero deve ser positivo!")

primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break

print(f"O número {numero} é primo" if primo and numero != 1 else f"O número {numero} não é primo")