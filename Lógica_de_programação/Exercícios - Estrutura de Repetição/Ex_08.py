print("""
    8. Faça um programa que leia 5 números e informe a soma e a média dos números.
""")

soma = 0
media = 0

controle = 0 
while controle != 5:
    n = input("Digite um número: ")
    numero = int(n)
    soma = soma + numero
    controle += 1 

# Calsulo da média
media = soma / 5
    
print('#-------------------------------------------------------#')
print(f'+ Soma: {"{:.2f}".format(soma)}')
print(f'Média: {"{:.2f}".format(media)}')
print('#-------------------------------------------------------#')