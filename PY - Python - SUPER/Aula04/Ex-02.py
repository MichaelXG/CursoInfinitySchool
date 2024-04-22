
def saudacao(valor_str: str) -> str:
    print(f'ola, {valor_str}, sejá bem vindo!')
    
nome = input('Digite seu nome:')

if nome is not None:
    saudacao(nome)