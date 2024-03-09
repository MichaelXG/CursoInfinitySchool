print("""
    25. Faça um programa que peça para n pessoas a sua idade, 
       ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
       e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
""")
soma_idade = 0
qtd_turma = 0
while qtd_turma <= 0:
    qtd_turma = int(input('Informe o número de pessoas da turma: '))
    if qtd_turma <= 0:
        print('Quantidade deve ser maior que zero!')
        
idades_l = []
idade_l = []

while len(idades_l) != qtd_turma:
    id_l = input(f'Digite a idade do {len(idades_l) + 1} aluno: ')
    idade_l = int(id_l)
    idades_l.append(id_l)
    soma_idade += idade_l

def calcular_media(nota, qtd) :
    media = (nota / qtd)
    return media 

media_turma = calcular_media(soma_idade, qtd_turma)

if media_turma > 0 and media_turma <= 25:
    faixa_turma = ', a turma é jovem.'
elif media_turma >= 26 and media_turma <= 60:
    faixa_turma = ', a turma é adulta.'
elif media_turma > 60:
    faixa_turma = ', a turma é idosa.'
    
print(f'A média é {calcular_media(soma_idade, qtd_turma)} {faixa_turma}')