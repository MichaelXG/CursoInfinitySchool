
add = {"Maça", "Banana", "Uva", "Morango"}

frutas = set()

frutas.update(add)

print(frutas)


print("Banana" in frutas)


frutas_vermehas = {"Morango","Cereja","Framboesa"}

for v in frutas_vermehas:
    print(v)
    
frutas_vermehas.remove('Cereja')
print(frutas_vermehas)


A = {1,2,3,4,10}
B = {5,9,6,7,9,8}

A.union(B)
print(A)

print(A.intersection(B))