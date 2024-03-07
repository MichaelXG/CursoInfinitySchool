print("""
    19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
""")
soma = 0
maior = 0
menor = 0
cont = 0

qtd_numeros = 0
while qtd_numeros <= 0:
    qtd_numeros = int(input('Quantos números deseja informar: '))
    if qtd_numeros <= 0:
        print('Quantidade deve ser maior que zero!')

numeros = []

while len(numeros) != qtd_numeros:
    n = input("Digite um número: ")
    numero = int(n)
    numeros.append(numero)
    
    if numero < 0 or numero > 1000:
        print("Ops! Algo está errado. Tente novamente...\nInforme apenas números entre [0 e 1000] \n")
        numeros.remove(numero)
    else:
         soma += numero

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