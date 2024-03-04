print("""
    4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
""")
    
nota1 = int(input("Informe um número 01: "))
nota2 = int(input("Informe um número 02: "))
nota3 = int(input("Informe um número 03: "))
nota4 = int(input("Informe um número 04: "))

def calcularMedia(nota1, nota2, nota3, nota4) :
   media = ((nota1 + nota2 + nota3 + nota4) / 4)
   return media 

print(f'A média é  {calcularMedia(nota1, nota2, nota3, nota4)}')