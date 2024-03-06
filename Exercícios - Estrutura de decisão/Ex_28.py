print("""
    28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
        
        Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
        porém não há limites para a quantidade de carne por cliente. 
        Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
        Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
        contendo as informações da compra: 
        tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
""")
print('#-------------------------------------------------------#')
print('#            ... Hipermercado Tabajara ...              #')
print('#-------------------------------------------------------#')
print('#   Qual o tipo de carne você deseja comprar ?          #')
print('#                                                       #')
print('#   1 - File Duplo                                      #')
print('#   2 - Alcatra                                         #')
print('#   3 - Picanha                                         #')
print('#-------------------------------------------------------# \n')

tipo_carne      = int(input('Informe o tipo de carne: '))
carne_kg        = float(input('Informe a quantidade de carne (KG) : '))
cartao_tabajara = input('Cartão Tabajara (S/N): ').upper()

def calcular_venda(tipo, kg):
    if tipo == 1:
        if kg <= 5:
            valor = kg * 4.9
        else:
            valor = kg * 5.8
    elif tipo == 2:
        if kg <= 5:
            valor = kg * 5.9
        else:
            valor = kg * 6.8
    elif tipo == 3:
        if kg <= 5:
            valor = kg * 6.9
        else:
            valor = kg * 7.8
    return valor

valor_bruto = calcular_venda(tipo_carne, carne_kg)

valor_desconto = 0.0

if cartao_tabajara == 'S':
    cartao_t = 'Sim'
    valor_desconto = valor_bruto * .05
else:
    cartao_t = 'Não'
    
# define o produto para exibir no cupom fiscal    
if tipo_carne == 1:
    produto = '1 - File Duplo'
elif tipo_carne == 2:
     produto = '2 - Alcatra'
elif tipo_carne == 3:
     produto = '3 - Picanha'
     
valor_pagar = valor_bruto - valor_desconto
valor_kg = valor_bruto / carne_kg

print('#-------------------------------------------------------#')
print('#            ... Hipermercado Tabajara ...              #')
print('#-------------------------------------------------------#')
print('#                    Cupom Fiscal                       #')
print('#-------------------------------------------------------#')
print(f'          Produto/KG : {produto} / {"{:.2f}".format(carne_kg)}  KG')
print(f'       Valor (KG) R$ : {"{:.2f}".format(valor_kg)}')
print(F'     Cartão Tabajara : {cartao_t}')
print(f'       - Desconto R$ : {"{:.2f}".format(valor_desconto)}')
print(f'  = Total à pagar R$ : {"{:.2f}".format(valor_pagar)}')
print('#-------------------------------------------------------# \n')