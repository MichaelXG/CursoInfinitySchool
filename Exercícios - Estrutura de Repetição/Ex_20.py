print("""
    20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
        e limitando o fatorial a números inteiros positivos e menores que 16.
""")

qtd_vezes = 0
while qtd_vezes <= 0:
    qtd_vezes = int(input('Quantas vezes deseja calcular o fatorial: '))
    if qtd_vezes <= 0:
        print('Quantidade deve ser maior que zero!')
        
numeros = []
numeros_fat = []

while len(numeros_fat) != qtd_vezes:
    n_fat = input("Digite um número para calcular o Fatorial: ")
    numero_fat = int(n_fat)
    numeros_fat.append(numero_fat)
    
    if numero_fat < 0 or numero_fat > 16:
        print("Ops! Algo está errado. Tente novamente...\nInforme apenas números  interiros entre [0 e 16] \n")
        numeros.remove(numero_fat)
        
print('#---------------------------------------------------#')
print('             Calculo do fatorial                     ')
print('#---------------------------------------------------#')
tamanho_lista = len(numeros_fat)
for f in range(tamanho_lista):
    fatorial = 1
    numero = numeros_fat[f]
    for n in range(1, numero + 1):
        numeros.append(n)
        fatorial *= n
        
    seguencia = sorted(numeros, reverse=True)
    seguencia = str(seguencia).replace("[", "")
    seguencia = str(seguencia).replace("]", "")    
    seguencia = str(seguencia).replace(",", ".")
    seguencia = str(seguencia).replace(" ", "")

    print(f'{numero}! = {seguencia} = {fatorial}')

    # Limpa as variaveis
    numeros = []
    fatorial = 0
print('#---------------------------------------------------#')