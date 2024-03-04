print("""
    16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
    que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
)

areaPintar = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

qtdLatas = 0
ValorlataTinta = 80
lataTinta = 18
cobertura = 3

qtdLatas = round(((areaPintar / cobertura) / lataTinta), 2)

qtdLatasInt = round(((areaPintar / cobertura) / lataTinta))

def validaLata(qtd_i, qtd_r):
    qtd = 0
    if (qtd_i + 1) > qtd_r:
        qtd = qtd_i + 1
    return qtd
    
qtdLatasFinal = validaLata(qtdLatasInt, qtdLatas)
   
ValorTotal = qtdLatasFinal * ValorlataTinta 

print('#---------------------------------------------------#')
print(f'A área a ser pintada é de {"{:.2f}".format(areaPintar)} metros quadrados, para pintar essa área precisamos de {"{:.2f}".format(qtdLatas)} litros de tinta \n')
print(f'Quantidades de latas de tinta (18 Litros) a serem compradas: {"{:.2f}".format(qtdLatasFinal)} \n')
print(f'= Preço total : R$ {"{:.2f}".format(ValorTotal)}')
print('#---------------------------------------------------#')
