print("""
    21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
        depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
        O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

        Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
        Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
                   uma nota de 5 e quatro notas de 1.
""")

valor_saque = float(input("Qual o valor do saque: "))

notas_100 = valor_saque // 100
valor_saque = valor_saque % 100

notas_50 = valor_saque // 50
valor_saque = valor_saque % 50

notas_20 = valor_saque // 20
valor_saque = valor_saque % 20

notas_10 = valor_saque // 10
valor_saque = valor_saque % 10

notas_5 = valor_saque // 5
valor_saque = valor_saque % 5

notas_2 = valor_saque // 2
valor_saque = valor_saque % 2

notas_1 = valor_saque // 1
valor_saque = valor_saque % 1

print('#---------------------------------------------------#')
print(f'Notas de  R$ 100 :{"{:.2f}".format(notas_100)}')
print(f'Notas de  R$  50 :{"{:.2f}".format(notas_50)}')
print(f'Notas de  R$  20 :{"{:.2f}".format(notas_20)}')
print(f'Notas de  R$  10 :{"{:.2f}".format(notas_10)}')
print(f'Notas de  R$   5 :{"{:.2f}".format(notas_5)}')
print(f'Notas de  R$   2 :{"{:.2f}".format(notas_2)}')
print(f'Notas de  R$   1 :{"{:.2f}".format(notas_1)}')

print('#---------------------------------------------------#')