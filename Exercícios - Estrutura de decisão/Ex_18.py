print("""
    18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
""")
# 
data = input('Informe uma data DD-MM-YYYY: ')

def valida_data(data_v):
    dia, mes, ano = map(int, data.split('-'))
    bissexto = False
    
    if (ano % 4 == 0):
        bissexto = True
    elif (ano % 100 == 0) and (ano % 400 != 0):
        bissexto = False

    if (mes in (1, 3, 5, 7, 8, 10, 12)):
        if (dia < 1) or (dia > 31):
            return False
        else:
            return True
    elif (mes in (4, 6, 9, 11)):
        if (dia < 1) or (dia > 30):
            return False
        else:
            return True
    else:
        if (bissexto):
            if (dia < 1) or (dia > 29):
                return False
            else:
                return True
        else:
            if (dia < 1) or (dia > 28):
                return False
            else:
                return True

print('#---------------------------------------------------#')
if valida_data(data) == True:
    print(f'A data {data} é válida')
else:
    print(f'A data {data} não é válida')
print('#---------------------------------------------------#')
