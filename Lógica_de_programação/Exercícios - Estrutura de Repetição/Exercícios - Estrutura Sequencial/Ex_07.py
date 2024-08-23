print("""
    7. Faça um Programa que calcule a área de um quadrado, 
       em seguida mostre o dobro desta área para o usuário.
"""
)
base = int(input("Informe a base: "))
altura = int(input("Informe a altura: "))

def calcularAreaQuadrado(base, altura):
   area = (base*altura) * 2
   return area

print(f'A área é {calcularAreaQuadrado(base, altura)}')
