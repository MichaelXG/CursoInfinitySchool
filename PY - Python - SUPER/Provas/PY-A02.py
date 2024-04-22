print("""
    [PY-A02] Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. 
    Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
    Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares 
    e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
""")


# Solicita ao usuário que digite 10 valores para preencher uma lista
valores = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Separa os números pares e ímpares em listas diferentes
pares = [num for num in valores if num % 2 == 0]
impares = [num for num in valores if num % 2 != 0]

# Exibe na tela os números pares, os números ímpares em uma tupla
print("Números pares:", pares)
print("Números ímpares:", tuple(impares))

# Exibe a quantidade de números pares e ímpares presentes na lista
print("Qtd. números pares:", len(pares))
print("Qtd. números ímpares:", len(impares))

# Exibe a soma de todos os números pares e ímpares, respectivamente
print("Soma dos números pares:", sum(pares))
print("Soma dos números ímpares:", sum(impares))

