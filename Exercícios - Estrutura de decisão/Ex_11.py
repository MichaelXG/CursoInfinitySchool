print("""
    11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
        desenvolver o programa que calculará os reajustes.
        
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        1. salários até R$ 280,00 (incluindo) : aumento de 20%
        2. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        3. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        4. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        5. o salário antes do reajuste;
        6. o percentual de aumento aplicado;
        7. o valor do aumento;
        8. o novo salário, após o aumento.
""")
# 
salario = float(input('Informe o valor do salário do colaborador: '))
    
if (salario <= 280.0):
    percentual = 20
elif (salario <= 700.0):
    percentual = 15
elif (salario <= 1500.0):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
salario_novo = salario + aumento

print('#---------------------------------------------------#')
print(f'Salário Bruto: R$ {"{:.2f}".format(salario)}')
print(f'% Aumento: {"{:.2f}".format(percentual)} %')
print(f'+ Valor Aumento  R$ {"{:.2f}".format(aumento)}')
print(f'= Novo Salário Liquido : R$ {"{:.2f}".format(salario_novo)}')
print('#---------------------------------------------------#')


