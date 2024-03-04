print("""
    6. Faça um Programa que leia três números e mostre o maior deles.
""")
# 
n1 = int(input("Informe um número 01: "))
n2 = int(input("Informe um número 02: "))
n3 = int(input("Informe um número 03: "))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3  
    
print('#---------------------------------------------------#')
print(f'O número maior é {"{:.2f}".format(maior)}')
print('#---------------------------------------------------#')