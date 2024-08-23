print("""
    2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
""")

n1 = int(input("Informe um número: "))

print('#---------------------------------------------------#')
if n1 > 0:
    print(f'{n1} é positivo')
elif n1 < 0:
    print(f'{n1} é negativo')
else:
    print('O número é igual a zero (0)')
print('#---------------------------------------------------#')
    


