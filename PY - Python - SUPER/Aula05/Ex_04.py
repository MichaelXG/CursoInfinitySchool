print("""
    ATIVIDADE PRÁTICA 4

    Crie uma função que aceita uma lista de números e use
    a função map para retornar uma nova lista contendo o
    dobro de cada número na lista de entrada.
""")

def dobro(lista =[]):
    result = []
    for n in lista:
        result.append(n * 2)
    return result
    
    
numeros = []
controle = -1 
while controle != 0:
    n = input("Digite um número inteiro: ")
    numero = int(n)
    if numero == 0:
        controle = 0
    else:  
        numeros.append(numero)
    
print(dobro(numeros))
    
    
