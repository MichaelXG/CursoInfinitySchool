print("""
    23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
        O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
        Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
""")
numeros_primos = []
qtd = 0
while (qtd <= 0):
    qtd = int(input('Voce quer saber os primeiros quantos números: '))
    if (qtd <= 0):
        print ('A quandidade deve ser positiva!')

qtd_div = 0
for numero in range(1, qtd + 1):
    primo = True
    for i in range(2, round(((numero / 2) + 1))):
        qtd_div += 1
        if (numero % i == 0):
            primo = False
            break          

    if (primo):
        numeros_primos.append(numero)

print(numeros_primos)
print(f'\nQuantidade de divisões: {qtd_div}')