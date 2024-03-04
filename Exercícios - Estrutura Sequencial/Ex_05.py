print("""
   5. Faça um Programa que converta metros para centímetros.
""")

metros = int(input("Informe quantos metros:"))

def converterMetrosEmCentimetos(metros):
   centimetros = metros * 100
   return centimetros

print(f'A conversão de {metros} metros é {converterMetrosEmCentimetos(metros)} centimetros.')