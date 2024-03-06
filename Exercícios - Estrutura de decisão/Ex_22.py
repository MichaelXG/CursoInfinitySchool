print("""
    22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
        Dica: utilize o operador módulo (resto da divisão).
""")
# 
n1 = int(input("Informe um número: "))

print('#---------------------------------------------------#')
if (n1 % 2 == 0):
    print(f'O número {"{:.2f}".format(n1)} é par')
else:
    print(f'O número {"{:.2f}".format(n1)} é impar')
print('#---------------------------------------------------#')