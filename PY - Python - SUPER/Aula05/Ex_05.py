print("""
    ATIVIDADE PRÁTICA 5

    Crie uma função que aceita uma lista de números e use
    a função filter para retornar uma nova lista contendo
    apenas os números pares da lista de entrada.
""")

def pares(lista =[]):
     return list(filter(lambda x: x % 2 == 0, lista))   
      
numeros = []
controle = -1 
while controle != 0:
    n = input("Digite um número inteiro: ")
    numero = int(n)
    if numero == 0:
        controle = 0
    else:  
        numeros.append(numero)
    
print(pares(numeros))