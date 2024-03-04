print("""
   12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
       usando a seguinte fórmula: (72.7*altura) - 58
"""
)
altura = float(input('Informe a altura de uma pessoa: '))

def calculoPesoIdeal(altura):
    pesoIdeal = (72.7*altura) - 58
    return pesoIdeal

print(f'Seu peso ideal é {calculoPesoIdeal(altura)} kilos')