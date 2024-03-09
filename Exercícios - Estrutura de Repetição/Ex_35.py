print("""
    35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes 
        entre 1 e um número inteiro informado pelo usuário.
""")

primos = []

n = 0
while (n <= 0):
    n = int(input('Verificar números primos até: '))
    if (n <= 0):
        print('O numero deve ser positivo!')

for numero in range(2, n + 1):
    primo = True
    for i in range(2, round(((numero / 2) + 1))):
        if (numero % i == 0):
            primo = False
            break          

    if (primo):
        primos.append(numero)

print(f'Números primos :{primos}')