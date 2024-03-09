print("""
    33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto 
        indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
""")
soma = 0
maior = 0
menor = 0
cont = 1

temperaturas = []

temp_al_top = \
("""
#-----------------------------------------------------#
#       Departamento Estadual de Meteorologia         #
#-----------------------------------------------------#
#  Atenção: Ao terminar de informar as temperaturas,  #
#  para concluir o processo precione a tecla "X"      #
#-----------------------------------------------------#
""")
def calcular_media(valor, qtd):
    media = (valor / qtd)
    return media 

print(temp_al_top)

controle = 'A'
while controle != 'X':
    t = input(f'Informe a temperaturas_{cont}: ')
    
    if t.upper() == "X":
         controle = "X"
         break
    
    temp = float((t).replace(",", "."))
    temperaturas.append(temp)
    cont += 1

    # if temp == 0:
    #     temperaturas.remove(temp)
    #     controle = 0

    # Soma dos números digitados    
    soma +=  temp

# Encontrar o maior número    
maior = temperaturas[0]
tamanho_lista = len(temperaturas)
for i in range(tamanho_lista):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        
# Encontrar o maior número    
menor = temperaturas[0]
tamanho_lista = len(temperaturas)
for i in range(tamanho_lista):
    if temperaturas[i] < menor:
        menor = temperaturas[i]

print('#-----------------------------------------------------#')
print(f'Temperaturas = {temperaturas} \n')
print(f' A menor temperatura é {"{:.2f}".format(menor)} Cº')
print(f' A maior temperatura é {"{:.2f}".format(maior)} Cº')
print(f' Média das temperaturas : {"{:.2f}".format(calcular_media(soma, cont))} Cº')
print('#-----------------------------------------------------#')