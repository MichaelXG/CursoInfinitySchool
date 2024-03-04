print("""
   13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
"""
)
sexo =  input('Informe seu sexo ("H - Homem" ou "M - Mulher"):')
altura = float(input('Informe a altura de uma pessoa: '))

if sexo == 'H' or sexo == 'h':
    sexoT = " o homen " 
elif sexo == 'M' or sexo == 'm':
    sexoT = "a mulher "

def calculoPesoIdeal(sexo, altura):
    if sexo == 'H' or sexo == 'h':
        pesoIdeal = (72.7*altura) - 58
    elif sexo == 'M' or sexo == 'm':
        pesoIdeal = (62.1*altura) - 44.7
    return pesoIdeal 

print(f'Seu peso ideal {sexoT} é  {calculoPesoIdeal(sexo, altura)} kilos')