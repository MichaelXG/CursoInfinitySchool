print("""
    15. Faça um Programa que peça os 3 lados de um triângulo.
        O programa deverá informar se os valores podem ser um triângulo. 
        Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
        
        Dicas:
        *. Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
        *. Triângulo Equilátero: três lados iguais;
        *. Triângulo Isósceles: quaisquer dois lados iguais;
        *. Triângulo Escaleno: três lados diferentes;
""")
# 

l1 = float(input('informe o lado 1 do triângulo: '))
l2 = float(input('informe o lado 2 do triângulo: '))
l3 = float(input('informe o lado 3 do triângulo: '))


def valida_triangulo(l1, l2, l3):
    if (l1 > (l2 + l3)) or (l2 > (l1 + l3)) or (l3 > (l1 + l2)):
        triangulo = False
    else:
        triangulo = True

    if (triangulo):
        # Triângulo Equilátero: três lados iguais;
        if (l1 == l2) and (l2 == l3):
            return  'Triângulo Equilátero'
        # Triângulo Isósceles: quaisquer dois lados iguais;
        elif (l1 == l2) or (l1 == l2) or (l2 == l3):
            return  'Triângulo Isósceles'
        else:
            return  'Triângulo Escaleno'
    else:
        return 'Os valores não formam um Triângulo'

print('#---------------------------------------------------#')
print(valida_triangulo(l1, l2, l3))
print('#---------------------------------------------------#')