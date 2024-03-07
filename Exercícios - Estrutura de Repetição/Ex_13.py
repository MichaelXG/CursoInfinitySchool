print("""
    13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
        Não utilize a função de potência da linguagem.
""")

base = int(input('Informe o valor da base: '))
expoente = 0
while (expoente <= 0):
    expoente = int(input('Informe o valor do expoente: '))
    if (expoente <= 0):
        print('O expoente deve ser positivo! \n')

potencia = 1
for i in range(1, expoente + 1):
    potencia *= base

print('#---------------------------------------------------#')
print(f'{base} elevada à {expoente} = {potencia}')
print('#---------------------------------------------------#')