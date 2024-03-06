print("""
    23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
        Dica: utilize uma função de arredondamento.
""")
# 
n1 = float(input("Informe um número: "))

print('#---------------------------------------------------#')
if (n1 == int(n1)):
    print(f'O número {n1} é inteiro')
else:
    print(f'O número {n1} é decimal')
print('#---------------------------------------------------#')