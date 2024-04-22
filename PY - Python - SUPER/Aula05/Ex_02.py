
print("""
   Crie uma função que recebe um número variável de nomes de amigos e cria uma lista com esses nomes 
   e imprima essa lista. 
""")


amigos = []

def amigos(*args):
    result = ''
    for amigo in args:
        amigos.append(amigo)
    return result
        
print(amigos('Amanda', 'aline','michele'))
        
        



        