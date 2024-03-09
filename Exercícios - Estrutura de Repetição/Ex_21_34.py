print("""
    21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
        Um número primo é aquele que é divisível somente por ele mesmo e por 1.
""")
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