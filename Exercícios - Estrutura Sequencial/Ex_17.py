print("""
    17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
        Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
        que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
        
        Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        a. comprar apenas latas de 18 litros;
        b. comprar apenas galões de 3,6 litros;
        c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os 
           valores para cima, isto é, considere latas cheias.
"""
)
area_pintar = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

qtd_latas = 0
valor_lata_tinta_18 = 80
valor_lata_tinta_3_6 = 25
lata_tinta_18 = 18
lata_tinta_3_6 = 3.6
cobertura = 6

lata_metro  =  18 * cobertura
galao_metro = 3.6 * cobertura

def valida_litros(area):
    litros = 0
    litro_r = round((area / cobertura), 2)
    litro_i = round(area / cobertura)
    if (litro_i) > litro_r:
        litros = litro_i
    elif (litro_i + 1) > litro_r:
        litros = litro_i + 1
    return litros
    
litros_utilizados = valida_litros(area_pintar)

def qntdLatas(litros_area, litros):
    qtd = 0
    qtd_r = round((litros_area / litros), 2)
    qtd_i = round(litros_area / litros)
    if (qtd_i + 1) > qtd_r:
        qtd = qtd_i + 1
    return qtd

qtd_latas_18 = qntdLatas(litros_utilizados, lata_tinta_18)
valor_total_18 = qtd_latas_18 * valor_lata_tinta_18 

qtd_latas_3_6 = qntdLatas(litros_utilizados, lata_tinta_3_6)
valor_total_3_6 = qtd_latas_3_6 * valor_lata_tinta_3_6 

#mistura

print('#---------------------------------------------------#')
print(f'A área a ser pintada é de {"{:.2f}".format(area_pintar)} metros quadrados, serão gastos {"{:.2f}".format(litros_utilizados)} Litros para pintar essa área. \n')

print('a. comprar apenas latas de 18 litros;')
print(f'Quantidades de latas de tinta (18 Litros) a serem compradas: {"{:.2f}".format(qtd_latas_18)} \n')
print(f'= Preço total : R$ {"{:.2f}".format(valor_total_18)} \n')

print('b. comprar apenas galões de 3,6 litros;')
print(f'Quantidades de latas de tinta (3,6 Litros) a serem compradas: {"{:.2f}".format(qtd_latas_3_6)} \n')
print(f'= Preço total : R$ {"{:.2f}".format(valor_total_3_6)} \n')

# print('c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os '
#       '   valores para cima, isto é, considere latas cheias. \n')
# print(f'Quantidades de latas de tinta (3,6 Litros) a serem compradas: {"{:.2f}".format(qtdLatas3_6)} \n')
# print(f'= Preço total : R$ {"{:.2f}".format(ValorTotal3_6)} \n')
print('#---------------------------------------------------#')
