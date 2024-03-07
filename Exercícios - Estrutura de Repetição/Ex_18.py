print("""
    18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
""")
soma = 0
maior = 0
menor = 0

qtd_numeros = 0
while qtd_numeros <= 0:
    qtd_numeros = int(input('Quantos números deseja informar: '))
    if qtd_numeros <= 0:
        print('Quantidade deve ser maior que zero!')

numeros = []

controle = 0 
while controle != qtd_numeros:
    n = input("Digite um número: ")
    numero = int(n)
    numeros.append(numero)
    soma += numero
    controle += 1

# Encontrar o maior número    
maior = numeros[0]
tamanho_lista = len(numeros)
for i in range(tamanho_lista):
    if numeros[i] > maior:
        maior = numeros[i]
        
# Encontrar o maior número    
menor = numeros[0]
tamanho_lista = len(numeros)
for i in range(tamanho_lista):
    if numeros[i] < menor:
        menor = numeros[i]

print('#-----------------------------------------------------------------------#')
print(f'numeros = {numeros} \n')
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
print(f'+ soma = {soma}')
print('#-----------------------------------------------------------------------#')