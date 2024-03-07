print("""
    12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
        O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
       
        Tabuada de 5:
        5 X 1 = 5
        5 X 2 = 10
        ...
        5 X 10 = 50
""")

numero_tab = int(input('Informe o número para gerar a  tabuada: '))

valida_ope = True
 
while valida_ope:
    operador  = input('Informe o operador: (+ . soma) | (- . subtração) | (* . multiplicação) | (/ . divisão): ')
    if ('+-*/'.find(operador) >= 0):
        valida_ope = False
    else:
        print("Ops! Algo está errado. Tente novamente... \n"\
              "Operador invalido! \n")
        
print('#---------------------------------------------------#')
print('#                    Tabuada                        #')
print('#---------------------------------------------------#')
i = 1
while i < 10:
    if operador == '+':
        calular = numero_tab + i  
    elif operador == '-':
        calular = numero_tab - i
    elif operador == '*':
        calular = numero_tab * i
    elif operador == '/':
        calular = numero_tab / i
    
    print(f'{numero_tab} {operador} {i} = {calular}')
    
    i += 1
print('#---------------------------------------------------#')