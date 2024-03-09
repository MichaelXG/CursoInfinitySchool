print("""
    22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
""")
divisoes = []
numero = 0
while (numero <= 0):
    numero = int(input('Verificar se o número é primo: '))
    if (numero <= 0):
        print('O numero deve ser positivo!')

primo = True
for i in range(2, numero):
    if (numero % i == 0):
        primo = False
       
            
if (primo):
    print (f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')

    for i in range(1, numero + 1):
        if (numero % i == 0):
            divisoes.append(i)
            
    print(f'O número {numero} é divisível por {divisoes}')