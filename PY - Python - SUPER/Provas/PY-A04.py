print("""
    [PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas.
    Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas 
    e calcular a média do aluno. 
    Também crie uma função chamada "verificar_situacao" que, com base na média calculada, 
    irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior 
    ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
""")


def calcular_media(valor) :
    total = sum(valor)
    qtd = len(valor)
    media = (total / qtd)
    return media 

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media >= 7 and media < 10:
        return "Aprovado"
    elif media >= 10: 
        return "Parabéns, sua média é 10"

def main():
    notas = []
    cont = -1
    while cont != 0:
        nota = float(input("Digite uma nota: "))
        if nota == 0:
            continua = input("Deseja adicionar mais notas? (s/n): ").lower() == "s"
            if continua:
                continue
            else:
                cont = 0
        else:
            notas.append(nota)

    if continua == 0:
        media = calcular_media(notas)
        situacao = verificar_situacao(media)

        print('#-------------------------------------------------------#')
        print(f"A média do aluno é: {media:.2f}")
        print(f"Situação do aluno: {situacao}")
        print('#-------------------------------------------------------#')

if __name__ == "__main__":
    main()
