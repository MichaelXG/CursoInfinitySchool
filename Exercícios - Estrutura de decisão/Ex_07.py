print("""
    7. Faça um Programa que leia três números e mostre o maior e o menor deles.
""")
# 
n1 = int(input("Informe um número 01: "))
n2 = int(input("Informe um número 02: "))
n3 = int(input("Informe um número 03: "))

maior = n1
menor = n1

# identificar o Maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3  

# identificar o menor    
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3  
    
print('#---------------------------------------------------#')
print(f'O número maior é {"{:.2f}".format(maior)} e o menor é {"{:.2f}".format(menor)}')
print('#---------------------------------------------------#')