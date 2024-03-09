print("""
    17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
        Ex.: 5!=5.4.3.2.1=120
""")

numeros = []
numero = int(input("Fatorial de: ") )

fatorial = 1
for n in range(1, numero + 1):
    numeros.append(n)
    fatorial *= n
       
seguencia = sorted(numeros, reverse=True)
seguencia = str(seguencia).replace("[", "")
seguencia = str(seguencia).replace("]", "")    
seguencia = str(seguencia).replace(",", ".")
seguencia = str(seguencia).replace(" ", "")

print('#---------------------------------------------------#')
print('             Calculo do fatorial                     ')
print('#---------------------------------------------------#')
print(f'{numero}! = {seguencia} = {fatorial}')
print('#---------------------------------------------------#')