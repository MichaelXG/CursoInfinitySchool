print("""
    11. Altere o programa anterior para mostrar no final a soma dos números.
""")

numero_ini = int(input('Informe o número inicial: '))
soma = 0
numero_fin = numero_ini
while (numero_fin <= numero_ini):
    numero_fin = int(input('Informe o número final: '))
    if (numero_fin <= numero_ini):
        print('O valor final deve ser maior que o valor final !')

numeros = []

while numero_ini <= numero_fin:
    numeros.append(numero_ini)
    soma = soma + numero_ini
    numero_ini += 1

print('#-------------------------------------------------------------------------------------------------#')
print(f'Numeros = {numeros} \n')
print(f'+ Soma = {soma} ')
print('#-------------------------------------------------------------------------------------------------#')