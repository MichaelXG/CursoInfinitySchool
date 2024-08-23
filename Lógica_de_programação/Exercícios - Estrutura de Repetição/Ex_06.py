print("""
    6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
       Depois modifique o programa para que ele mostre os números um ao lado do outro. 
""")

numeros = []
num = 1
while num <= 20:
    print(num)
    numeros.append(num)
    num += 1

print('#-----------------------------------------------------------------------#')
print(numeros)
print('#-----------------------------------------------------------------------#')