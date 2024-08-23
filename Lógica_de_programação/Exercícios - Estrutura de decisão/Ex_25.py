print("""
    25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
        a. "Telefonou para a vítima?"
        b. "Esteve no local do crime?"
        c. "Mora perto da vítima?"
        d. "Devia para a vítima?"
        e. "Já trabalhou com a vítima?" 
        
        O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
        Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
        e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
""")
print('#-------------------------------------------------------#')
print('#                   ... Atenção ...                     #')
print('#  Responda as perguntas abaixo com S (sim) ou N (não)  #')
print('#-------------------------------------------------------# \n')
p1 = input('Telefonou para a vítima ? ').upper()
p2 = input('Esteve no local do crime ? ').upper()
p3 = input('Mora perto da vítima ? ').upper()
p4 = input('Devia para a vítima ? ').upper()
p5 = input('Já trabalhou com a vítima ? ').upper()

classificacao = 0

if (p1 == 'S'):
    classificacao += 1

if (p2 == 'S'):
    classificacao += 1

if (p3 == 'S'):
    classificacao += 1

if (p4 == 'S'):
    classificacao += 1

if (p5 == 'S'):
    classificacao += 1

print('#-------------------------------------------------------#')
if (classificacao < 2):
    print('Inocente')
elif (classificacao == 2):
    print('Suspeito')
elif (classificacao <= 4):
    print('Cumplice')
else:
    print('Assassino')
print('#-------------------------------------------------------#')