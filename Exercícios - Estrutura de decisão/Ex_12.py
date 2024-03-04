print("""
    12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
        que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
        mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
        O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
        
        Desconto do IR:
        *. Salário Bruto até 900 (inclusive) - isento
        *. Salário Bruto até 1500 (inclusive) - desconto de 5%
        *. Salário Bruto até 2500 (inclusive) - desconto de 10%
        *. Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
        
        No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
""")
# 
valor_Hora = float(input('Quanto ganha por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = valor_Hora * horas_trabalhadas

# Calcula o imposto de renda
if (salario_bruto > 2500):
    aliquota_ir = 20
elif (salario_bruto > 1500):
    aliquota_ir = 10
elif (salario_bruto > 900):
    aliquota_ir = 5
else:
    aliquota_ir = 0
    
valor_ir = salario_bruto * (aliquota_ir / 100)
fgts = salario_bruto * (11 / 100.0)
inss = salario_bruto * (10 / 100.0)
sindicato = salario_bruto *  (3 / 100.0)

descontos = valor_ir + inss

salario_liquido =  salario_bruto - descontos
print('#---------------------------------------------------#')
print(f'+ Salário Bruto             : R$ {"{:.2f}".format(salario_bruto)}')
print(f'- IR ({aliquota_ir} %)           : R$ {"{:.2f}".format(valor_ir)}')
print(f'- INSS (10%)                : R$ {"{:.2f}".format(inss)}')
print(f'- FGTS (11%)                : R$ {"{:.2f}".format(fgts)}')
print(f'- Sindicato (3%)            : R$ {"{:.2f}".format(sindicato)}')
print(f'= Descontos                 : R$ {"{:.2f}".format(descontos)}')
print(f'= Salário Liquido           : R$ {"{:.2f}".format(salario_liquido)}')
print('#---------------------------------------------------#')