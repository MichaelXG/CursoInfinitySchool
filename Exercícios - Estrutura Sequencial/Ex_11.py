print("""
   11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
       a. o produto do dobro do primeiro com metade do segundo .
       b. a soma do triplo do primeiro com o terceiro.
       c. o terceiro elevado ao cubo.
"""
)
n1 = int(input('Informe o número inteiro 01: '))
n2 = int(input('Informe o número inteiro 02: '))
n3 = float(input('Informe o número real 03: '))

print('#---------------------------------------------------#')
print (f'Produto: {((2*n1) * (n2/2))}')
print (f'Soma: {((3 * n1) + n3)}')
print (f'Cubo: {(n3**3)}')
print('#---------------------------------------------------#')
