print("""
    28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
        e o valor médio gasto em cada um deles.
        O usuário deverá informar a quantidade de CDs e o valor para em cada um.
""")
soma_cds = 0

def calcular_media(valor, qtd) :
    media = (valor / qtd)
    return media 

qtd_cds = 0
while qtd_cds <= 0:
    qtd_cds = int(input('Informe a quantidade de Cd''s: '))
    if qtd_cds <= 0:
        print('Quantidade deve ser maior que zero!')

valores_cds = []

while len(valores_cds) != qtd_cds:
    v_cds = input(f'Informe o valor do CD_{len(valores_cds) + 1}: ')
    valor_cds = float(v_cds)
    valores_cds.append(int(valor_cds))
    
    if valor_cds < 0:
        print("Ops! Algo está errado. Tente novamente...\nO Valor dos cd''s deve ser maior que zero.\n")
        valores_cds.remove(valor_cds)
    else:
         soma_cds += valor_cds

print(soma_cds)
print(f'\nO valor médio gasto em cada um foi {calcular_media(soma_cds, qtd_cds)}')
