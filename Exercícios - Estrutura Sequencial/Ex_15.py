print("""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
    descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.

    calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
"""
)

valorHora = float(input('Quanto ganha por hora? '))
horasTrabalhadas = int(input('Horas trabalhadas por mês: '))

salarioBruto = valorHora * horasTrabalhadas
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

print('#---------------------------------------------------#')
print(f'+ Salário Bruto: R$ {"{:.2f}".format(salarioBruto)}')
print(f'- IR: R$ {"{:.2f}".format(ir)}')
print(f'- INSS: R$ {"{:.2f}".format(inss)}')
print(f'- Sindicato: R$ {"{:.2f}".format(sindicato)}')
print(f'= Salário Liquido : R$ {"{:.2f}".format(salarioBruto - ir - inss - sindicato)}')
print('#---------------------------------------------------#')
