print("""
    5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
       Valide a entrada e permita repetir a operação..
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