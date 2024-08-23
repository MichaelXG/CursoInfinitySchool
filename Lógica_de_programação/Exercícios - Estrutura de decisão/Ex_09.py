print("""
    9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
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

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

meio = n1

if n2 > menor and n2 < maior:
    meio = n2
if n3 > menor and n3 < maior:
    meio = n3

print('#---------------------------------------------------#')
print(menor, meio, maior)
print(maior, meio, menor)
print('#---------------------------------------------------#')
