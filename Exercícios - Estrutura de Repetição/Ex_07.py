print("""
    7. Faça um programa que leia 5 números e informe o maior número.
""")

numeros = []

controle = 0 
while controle != 5:
    n = input("Digite um número: ")
    numero = int(n)
    numeros.append(numero)
    controle += 1

maior = numeros[0]
tamanho_lista = len(numeros)
for i in range(tamanho_lista):
    if numeros[i] > maior:
        maior = numeros[i]

print('#-----------------------------------------------------------------------#')
print(f'numeros = [{numeros}] \n')
print(f' O maior número é {maior}')
print('#-----------------------------------------------------------------------#')