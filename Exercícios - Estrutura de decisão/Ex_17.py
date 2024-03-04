print("""
    17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
""")
# 

ano = int(input('informe um ano (Ex: 1985): '))

def valida_ano_bissexto(ano):
    if (ano % 4 == 0):
        return True
    elif (ano % 100 == 0) and (ano % 400 != 0):
        return False

bissexto = valida_ano_bissexto(ano)

print('#---------------------------------------------------#')
if bissexto:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')
print('#---------------------------------------------------#')
