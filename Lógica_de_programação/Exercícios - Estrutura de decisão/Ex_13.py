print("""
    13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
""")
# 
controle = True

while controle:
    dia = int(input("Informe um número(1 - 7): "))
    
    if dia < 0 or dia > 7:
        print("Ops! Algo está errado. Tente novamente... \n")
    else:
        controle = False

def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-Feira"
    elif dia == 3:
        return "Terça-Feira"
    elif dia == 4:
        return "Quarta-Feira"
    elif dia == 5:
        return "Quinta-Feira"
    elif dia == 6:
        return "Sexta-Feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "Valor {} inválido".format(dia)
    
print('#---------------------------------------------------#')
print(dia_semana(dia))
print('#---------------------------------------------------#')