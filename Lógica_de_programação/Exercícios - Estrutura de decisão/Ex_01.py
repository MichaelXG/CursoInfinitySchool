print("""
    1. Faça um Programa que peça dois números e imprima o maior deles.
""")

n1 = int(input("Informe um número 01: "))
n2 = int(input("Informe um número 02: "))

if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2

print('#---------------------------------------------------#')
print(f'O maior número é {"{:.2f}".format(maior)}')
print('#---------------------------------------------------#')