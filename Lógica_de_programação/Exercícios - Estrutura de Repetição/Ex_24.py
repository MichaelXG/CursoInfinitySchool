import metodos

print("""
    24. Faça um programa que calcule o mostre a média aritmética de N notas.
""")
soma_nota = 0
qtd_notas = 0
while qtd_notas <= 0:
    qtd_notas = int(input('Quantas notas deseja lançar: '))
    if qtd_notas <= 0:
        print('Quantidade deve ser maior que zero!')
        
notas_l = []
nota_l = []

while len(notas_l) != qtd_notas:
    n_l = input(f'Digite a nota número_{len(notas_l) + 1}: ')
    nota_l = int(n_l)
    notas_l.append(nota_l)
    soma_nota += nota_l

print(f'A média é {calcular_media(soma_nota, qtd_notas)}')