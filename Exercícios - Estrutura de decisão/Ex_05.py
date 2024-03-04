print("""
    5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno 
       e apresentar:
       a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
       b. A mensagem "Reprovado", se a média for menor do que sete;
       c. A mensagem "Aprovado com Distinção", se a média for igual a dez
""")
# 
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2.0

print('#---------------------------------------------------#')
print(f'A media do aluno é {"{:.2f}".format(media)} \n')
if (media == 10):
     print(f'{"{:.2f}".format(media)} - Aprovado com Distinção')
elif (media >= 7):
    print(f'{"{:.2f}".format(media)} - Aprovado')
else:
     print(f'{"{:.2f}".format(media)} - Reprovado')
print('#---------------------------------------------------#')