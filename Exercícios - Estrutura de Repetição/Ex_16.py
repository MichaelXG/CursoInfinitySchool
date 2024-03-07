print("""
    16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
        Faça um programa que gere a série até que o valor seja maior que 500.
""")


controle = 0
inicial = 0
final = 1
primeiro = 0
num = 0
fibonacci = []

numero = 500 #int(input("Digite o n−ésimo termo da série: "))

fibonacci.append(final)
while controle <= numero - 1:
    inicial = final + inicial
    fibonacci.append(inicial)
    final = inicial + final
    fibonacci.append(final)
    controle += 1
print('#---------------------------------------------------#')
print('             Seqüência fibonacci                     ')
print('#---------------------------------------------------#')
print(f'seqüência fibonacci = {fibonacci}')
print('#---------------------------------------------------#')