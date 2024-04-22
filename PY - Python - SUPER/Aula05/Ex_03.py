print("""
    ATIVIDADE PRÁTICA 3

    Crie uma função chamada concatenar_strings que
    aceita um número variável de strings como argumentos
    posicionais (usando *args). A função deve concatenar
    todas as strings em uma única string e retorná-la.
""")

def concatenar(*args):
    result = ''
    for letra in args:
        result += letra
    return result

print(concatenar('b','a','n','a','n','a',))