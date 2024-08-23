print("""
    9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
""")

numeros = []
num = 1
while num <= 50:
    if (num % 2 != 0):
        numeros.append(num)
    num += 1

print('#-------------------------------------------------------------------------------------------------#')
print(numeros)
print('#-------------------------------------------------------------------------------------------------#')