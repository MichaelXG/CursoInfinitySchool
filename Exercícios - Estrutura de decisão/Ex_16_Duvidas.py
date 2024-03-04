print("""
    16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
    
        O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
        *. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir 
           os demais valores, sendo encerrado;
        *. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
        *. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
        *. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
""")
# 
import math

valor_a = float(input('informe o valor de a: '))
valor_b = float(input('informe o valor de b: '))
valor_c = float(input('informe o valor de c: '))

print('#---------------------------------------------------#')
# Valida se é uma equação de segundo grau
if (valor_a == 0):
    print('Não é uma equação de segundo grau')
else:
    # Delta - O math.pow() retorna o valor de x elevado à potência y.
    delta = math.pow(valor_b, 2) - (4 * valor_a * valor_c)

    if (delta < 0):
        print('A equação inválida, não possui valores reais.')
    elif (delta == 0):
        print('A equação possui apenas uma raiz')
        raiz = -(valor_b) / (2 * valor_a)
        print(f'Raíz :  {"{:.2f}".format(raiz)}')
    else:
        print('A equação possui duas raizes')
        raiz1 = (-(valor_b) + math.sqrt(delta)) / (2 * valor_a)
        raiz2 = (-(valor_b) - math.sqrt(delta)) / (2 * valor_a)
        print(f'Raíz 01:  {"{:.2f}".format(raiz1)}')
        print(f'Raíz 02:  {"{:.2f}".format(raiz2)}')   
print('#---------------------------------------------------#')