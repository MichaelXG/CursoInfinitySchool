

print("""
    Listas:

# Crie um algoritmo que dado um número, imprime uma lista que contém daquele número, até 0, em ordem decrescente.
# Ex: 10,  lista_final = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10] 
""")
numeros = []

numero = int(input('Informe o número: '))

for n in range(numero + 1):
    numeros.append(n)

print(f'Números Crescente: {numeros}')
print(f'Números Decrescente: {sorted(numeros, reverse=True)}')

