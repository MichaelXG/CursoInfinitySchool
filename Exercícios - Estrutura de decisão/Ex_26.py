print("""
    26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

        1. Álcool:
            a. até 20 litros, desconto de 3% por litro
            b. acima de 20 litros, desconto de 5% por litro

        2. Gasolina:
            a. até 20 litros, desconto de 4% por litro
            b. acima de 20 litros, desconto de 6% por litro 
        
        Escreva um algoritmo que leia o número de litros vendidos, 
        o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
        calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
        preço do litro da gasolina é R$ 2,50 
        o preço do litro do álcool é R$ 1,90.
""")
print('#-------------------------------------------------------#')
print('#            ... Posto de Gasolina ...                  #')
print('#-------------------------------------------------------# \n')

tipo_combustivel = input('Informe o tipo de combustível (A) para Alcool ou (G) para Gasolina: ').upper()
quantidade_litros = float(input('Informe a quantidade de litros: '))

if (tipo_combustivel == 'A'):
    valor = 1.9
    if (quantidade_litros <= 20):
        desconto = 3
    else:
        desconto = 5
else:
    valor = 2.5
    if (quantidade_litros <= 20):
        desconto = 4
    else:
        desconto = 6

# Valor a ser pago pelo cliente
total_pagar = (valor * quantidade_litros) * ((100 - desconto) / 100.0)

print('#-------------------------------------------------------#')
print(f'Valor a ser pago pelo cliente : R$ {"{:.2f}".format(total_pagar)}')
print('#-------------------------------------------------------#')