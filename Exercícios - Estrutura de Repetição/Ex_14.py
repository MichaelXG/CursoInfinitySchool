print("""
    14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
""")

numeros = []
par = 0
impar = 0

controle = 0 
while controle != 10:
    n = input("Digite um número inteiro: ")
    numero = int(n)
    numeros.append(numero)
    if (numero % 2 == 0):
        par += 1
    else:
        impar += 1
    controle += 1

print('#---------------------------------------------------#')
print(f'Numeros = {numeros}')
print(f'Qtd. número pares: {par}')
print(f'qtd. número impares : {impar}')
print('#---------------------------------------------------#')