n1 = 2
n2 = 3
n3 = 4
n4 = 4
pl = "palavra"

# 
print(f"Maior que    : {n1} >  {n2} = {n1 > n2}")
print(f"Menor que    : {n1} <  {n2} = {n1 < n2}")
print(f"Igual a      : {n1} == {n2} = {n1 == n2}")
print(f"Diferente de : {n1} != {n2} = {n1 != n2}")
print(f"Maior-igual  : {n1} >= {n2} = {n1 >= n2}")
print(f"Menor-igual  : {n1} <= {n2} = {n1 <= n2}")
print(f"Menor-igual  : {n1} <= {n2} = {n1 <= n2}")

p = str(input('Pesquise a palavra: '))
print(f"Está contido/contém  : {p in pl}")

p = str(input('Pesquise a palavra: '))
print(f"Não está contido/não contém  : {p not in pl}")