print("""
    36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
        mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser 
        informados também pelo usuário, conforme exemplo abaixo:
        
        Montar a tabuada de: 5
        Começar por: 4
        Terminar em: 7

        Vou montar a tabuada de 5 começando em 4 e terminando em 7:
        5 X 4 = 20
        5 X 5 = 25
        5 X 6 = 30
        5 X 7 = 35
        
        Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
""")
numero_tab = int(input('Montar a tabuada de: '))
numero_tab_ini = int(input('Começar por: '))
numero_tab_fin = int(input('Terminar em: '))

while numero_tab_fin <= numero_tab_ini:
    print("Ops! Algo está errado. Tente novamente...\nO termino não pode ser menos que o começo.\n")
    numero_tab_ini = int(input('Começar por: '))
    numero_tab_fin = int(input('Terminar em: '))
    

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
i = numero_tab_ini
while i < numero_tab_fin + 1:
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