print("""
    4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
       e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
       Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale 
       a população do país B, mantidas as taxas de crescimento.
""")
# Variaveis população A
populacao_A = 80000
crescimento_A = 1.03

# Variaveis população B
populacao_B = 200000
crescimento_B = 1.015

ano = 1
while (populacao_A <= populacao_B):
    populacao_A *= crescimento_A
    populacao_B *= crescimento_B
    ano += 1

print('#-------------------------------------------------------#')
print(f'Serão necessários, {ano} anos para que a população do país A \n'\
       'ultrapasse ou iguale a população do país B')
print('#-------------------------------------------------------#')