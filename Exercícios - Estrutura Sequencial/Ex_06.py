print("""
   6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
 """)

raio = float(input("Informe raio de um círculo: "))

def calcularAreaCirculo(raio):
   pi = 3.14
   area = pi * (raio**2)
   return area

print(f'A área é {calcularAreaCirculo(raio)}')
