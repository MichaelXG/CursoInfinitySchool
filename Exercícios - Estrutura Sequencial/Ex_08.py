print("""
   8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
      Calcule e mostre o total do seu salário no referido mês.
"""
)
valorHora = float(input('Quanto ganha por hora? '))
horasTrabalhadas = int(input('Horas trabalhadas por mês: '))

def calcularSalario(valorHora, horasTrabalhadas):
   salario = (valorHora*horasTrabalhadas)
   return salario

print(f'O salário no referido mês {calcularSalario(valorHora, horasTrabalhadas)}')
