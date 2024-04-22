

print("""
    Listas:

2: Dada a seguinte lista:
animais = ["foca", "golfinho", "leão", "tartaruga"]
Crie um algoritmo que imprima o primero e o último item da lista.

""")

animais = ["foca", "golfinho", "leão", "tartaruga"]

print('#-----------------------------------------------------------------------#')
tamanho_lista = len(animais)

for i in range(tamanho_lista):
    if i == 0 or i == tamanho_lista - 1:
        print(f'{animais[i]}')
    else:
        continue
print('#-----------------------------------------------------------------------#')