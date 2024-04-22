print("""
    ATIVIDADE PRÁTICA 6

    Crie uma função que aceita uma lista de strings e use a
    função reduce (importada de functools) para encontrar

    a maior string na lista.
""")

def maiorStr(a, b):
    print(a, b)
    if len(a) > len(b):
        return a
    else:
        return b
    
from functools import reduce

produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro", "amoreira", "azulejo"] 
maior = reduce(maiorStr, produtos)
print(maior)