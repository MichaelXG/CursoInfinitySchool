print("""
    27. Faça um programa que calcule o número médio de alunos por turma. 
        Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
        As turmas não podem ter mais de 40 alunos
""")

limite_turma = 40
soma_alunos = 0

def calcular_media(valor, qtd) :
    media = (valor / qtd)
    return media 

qtd_turma = 0
while qtd_turma <= 0:
    qtd_turma = int(input('Informe a quantidade de turmas: '))
    if qtd_turma <= 0:
        print('Quantidade deve ser maior que zero!')

alunos_sala = []

while len(alunos_sala) != qtd_turma:
    alunos_s = input(f'Informa a quantidade de alunos para cada turma_{len(alunos_sala) + 1}: ')
    alunos = int(alunos_s)
    alunos_sala.append(int(alunos))
    
    if alunos < 0 or alunos > limite_turma:
        print("Ops! Algo está errado. Tente novamente...\nAs turmas não podem ter mais de 40 alunos. \n")
        alunos_sala.remove(alunos)
    else:
         soma_alunos += alunos

print(f'\nO número médio de alunos por turma é {calcular_media(soma_alunos, qtd_turma)}')
