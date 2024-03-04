print("""
    14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
        e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  
        Média de Aproveitamento  Conceito
        Entre 9.0 e 10.0        A
        Entre 7.5 e 9.0         B
        Entre 6.0 e 7.5         C
        Entre 4.0 e 6.0         D
        Entre 4.0 e zero        E
""")
# 

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2.0

if (media < 4):
    conceito = 'E'
    aprovado = False
elif (media < 6):
    conceito = 'D'
    aprovado = False
elif (media < 7.5):
    conceito = 'C'
    aprovado = True
elif (media < 9):
    conceito = 'B'
    aprovado = True
else:
    conceito = 'A'
    aprovado = True

if (aprovado):
    aprovado_r = 'APROVADO'
else:
    aprovado_r = 'REPROVADO'

print('#---------------------------------------------------#')
print(f'A media do aluno é {"{:.2f}".format(media)} \n')

print(f'Seu Conceito é {conceito} por isso o aluno está {aprovado_r}')
print('#---------------------------------------------------#')