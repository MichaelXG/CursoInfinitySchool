

print("""
    Listas:

    1: Crie um algoritmo que, ao declararmos uma lista com o amigo de três amigos, imprima:
    o amigo do primeiro amigo
    o amigo do segundo amigo
    o amigo do terceiro amigo
""")

amigos = []
str_amigo = ''

controle = 0 
while controle != 3:
    amigo = input("Digite um amigo: ")
    amigos.append(amigo)
    controle += 1

print('#-----------------------------------------------------------------------#')
tamanho_lista = len(amigos)

for i in range(tamanho_lista):
    if i == 0:
        str_amigo = 'Primeiro Amigo : -->'
    elif i == 1:
        str_amigo = 'Segundo Amigo : -->'
    elif i == 2:
        str_amigo = 'Terceiro Amigo : -->'    

    print(f'{str_amigo} {amigos[i]}')
print('#-----------------------------------------------------------------------#')