

print("""
    Listas:


 9: Dada duas listas:
    nomes = ["Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"]
    sobrenomes = ["Silva", "Oliveira", "Rocha", "Marques", "Amaral"]
    Crie um algoritmo que construa uma tupla com os valores nome + sobrenome correspondentes;
    Essas listas são correspondentes, então a primeira pessoa é "Bruna" e seu sobrenome é "Silva".
""")


nomes = ["Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"]
sobrenomes = ["Silva", "Oliveira", "Rocha", "Marques", "Amaral"]

tupla = []
tamanho_lista_n =  len(nomes)
tamanho_lista_s =  len(sobrenomes)

nova_tupla =[]

for i in range(tamanho_lista_n):
     nova_tupla.append((nomes[i], sobrenomes[i]))

print(f'Tupla: {nova_tupla}')