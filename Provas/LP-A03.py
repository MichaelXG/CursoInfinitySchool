print("""
    [LP-A03] Escreva um programa em python que leia números inteiros do teclado. 
             O programa deve ler os números até que o usuário digite 0 (zero). 
             No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
""")

soma = 0
quantidade = 0
media = 0

controle = -1 
while controle != 0:
    n = input("Digite um número inteiro: ")
    
    numero = int(n)

    if numero == 0:
        controle = 0
    
    # Soma dos números digitados    
    soma = soma + numero
    
    # Zero por ser a condição de controle não entra na soma da quantidade5
    if numero != 0:
        quantidade += 1

# Calsulo da média
media = soma / quantidade
    
print('#-------------------------------------------------------#')
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f'Média: {"{:.2f}".format(media)}')
print('#-------------------------------------------------------#')

