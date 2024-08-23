print("""
    10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
""")

numero_ini = int(input('Informe o número inicial: '))

numero_fin = numero_ini
while (numero_fin <= numero_ini):
    numero_fin = int(input('Informe o número final: '))
    if (numero_fin <= numero_ini):
        print('O valor final deve ser maior que o valor final !')

numeros = []

while numero_ini <= numero_fin:
    numeros.append(numero_ini)
    numero_ini += 1

print('#-------------------------------------------------------------------------------------------------#')
print(numeros)
print('#-------------------------------------------------------------------------------------------------#')