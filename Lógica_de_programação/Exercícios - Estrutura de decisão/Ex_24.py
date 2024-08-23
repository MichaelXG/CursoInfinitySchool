print("""
    24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
        O resultado da operação deve ser acompanhado de uma frase que diga se o número é:       
        a. par ou ímpar;
        b. positivo ou negativo;
        c. inteiro ou decimal.
""")
print('#---------------------------------------------------#')
n1 = float(input("Informe um número 01: "))
n2 = float(input("Informe um número 02: "))
print("""
      Qual o tipo de operação você deseja realiza ?
    
        1 -  + (adição): soma dois valores.
        2 - – (subtração): subtrai o segundo valor do primeiro valor.
        3 -  * (multiplicação): multiplica dois valores.
        4 -  / (divisão): divide o primeiro valor pelo segundo valor.
        5 -  % (módulo): retorna o resto da divisão do primeiro valor pelo segundo valor.
        6 -  ** (exponenciação): eleva o primeiro valor à potência do segundo valor.
        7 - // (divisão inteira): divide o primeiro valor pelo segundo valor ignorando a parte decimal.
""")

controle  = True
par       = False
positivo  = False
inteiro   = False

def valida_par_impar(numero):
    if (int(numero) % 2 == 0):
        return True
    else:
        return False
    
def valida_positivo_negativo(numero):  
    if int(numero) > 0:
        return True
    elif int(numero) < 0:
        return False

def valida_inteiro_decinal(numero):   
    if (float(numero) == int(numero)):
        return True
    else:
        return False

while controle:
    ope = int(input("Informe o tipo de operação de [1 - 7]: "))

    if ope < 0 or ope > 7:
        print("Ops! Algo está errado. Tente novamente...")
    else:
        controle = False
    
def tipo_operacao(ope):
    if ope == 1:       # + (adição): soma dois valores.
        resultado = n1 + n2
        return resultado
    elif ope == 2:     # – (subtração): subtrai o segundo valor do primeiro valor.
        resultado = n1 - n2
        return resultado
    elif ope == 3:     # * (multiplicação): multiplica dois valores.
        resultado = n1 * n2
        return resultado
    elif ope == 4:     # / (divisão): divide o primeiro valor pelo segundo valor.
        resultado = n1 / n2
        return resultado
    elif ope == 5:     # % (módulo): retorna o resto da divisão do primeiro valor pelo segundo valor.
        resultado = n1 % n2
        return resultado
    elif ope == 6:     # ** (exponenciação): eleva o primeiro valor à potência do segundo valor.
        resultado = n1 ** n2
        return resultado
    elif ope == 7:     # // (divisão inteira): divide o primeiro valor pelo segundo valor ignorando a parte decimal.
        resultado = n1 // n2
        return resultado
    else:
        return "operador {} inválido".format(ope)
    
if not controle:
    result    = tipo_operacao(ope)
    par       = valida_par_impar(result)
    positivo  = valida_positivo_negativo(result)
    inteiro   = valida_inteiro_decinal(result)
    
    print('#---------------------------------------------------#')
    print(f'Resultado: {result}')
    if par:
        print('É Par')
    else:
         print('É Impar')
    if positivo:
        print('É Positivo')
    else:
         print('É Negativo')    
    if inteiro:
        print('É Inteiro')
    else:
         print('É Descimal')     
    print('#---------------------------------------------------#')