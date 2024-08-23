print("""
    19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
        
        Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
        326 = 3 centenas, 2 dezenas e 6 unidades
        12 = 1 dezena e 2 unidades 
        Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
""")
# 

controle = True

while controle:
    num = input("Informe um numero inteiro (< 1000): ")

    if int(num) < 0 or int(num) > 1000:
        print("Ops! Algo está errado. Tente novamente... \n")
    else:
        controle = False
    
numero = int(num)

centena = numero // 100
numero = numero % 100

dezena = numero // 10
numero = numero % 10

unidade = numero // 1
numero = numero % 1

resultado = ''

if centena > 0:
    if centena == 1:
        resultado = str(centena) + ' centena, '
    elif centena > 1:
        resultado = str(centena) + ' centenas, '
        
if dezena > 0:
    if dezena == 1:
        resultado = resultado + str(dezena) + ' dezena '
    elif dezena > 1:
        resultado = resultado + str(dezena) + ' dezenas '  
elif dezena == 0:
    if len(num) == 2:
        resultado = str(dezena) + ' dezena  '
    elif len(num) == 3:
        if dezena == 1 or dezena == 0:
            resultado = resultado + str(dezena) + ' dezena '
        elif dezena > 1:
            resultado = resultado + str(dezena) + ' dezenas '  
    
if unidade > 0:
    if len(num) == 1:
        if unidade == 1:
            resultado = str(unidade) + ' unidade '
        elif unidade > 1:
            resultado = str(unidade) + ' unidades '  
    else:    
        if unidade == 1:
            resultado = resultado + 'e ' +str(unidade) + ' unidade '
        elif unidade > 1:
            resultado =  resultado + 'e ' + str(unidade) + ' unidades '  
elif unidade == 0:
    if len(num) == 2:
        if unidade == 1 or unidade == 0:
            resultado = resultado + 'e ' + str(unidade) + ' unidade '
        elif unidade > 1:
            resultado =  resultado + 'e ' + str(unidade) + ' unidades '   
    elif len(num) == 3:
        if unidade == 1 or unidade == 0:
            resultado = resultado + 'e ' +str(unidade) + ' unidade '
        elif unidade > 1:
            resultado = resultado + 'e ' + str(unidade) + ' unidades ' 
        
print('#-------------------------------------------------------#')
print(resultado)
print('#-------------------------------------------------------#')

