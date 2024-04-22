

print("""
    Listas:


# 5: Dada a seguinte lista:
# produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]
# Crie um algoritmo que ao receber essa lista imprima os itens que iniciam com a letra "a"
""")


produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]

nova_lista = []
tamanho_lista =  len(produtos)

for pro in range(tamanho_lista):
    if ('A'.find(produtos[pro][0].upper()) >= 0):
        nova_lista.append(produtos[pro])

print(f'Nova Lista: {nova_lista}')