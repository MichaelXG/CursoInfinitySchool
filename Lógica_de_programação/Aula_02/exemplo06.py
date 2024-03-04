print(
"""
MENU DIGITAL DA CLARO - A PIOR OPERADORA DO BRASIL

1 - Mudança de Plano
2 - Cobranças
3 - Suporte Técnico
4 - Segunda Via de Contas
5 - Falar com o Atendente
"""
)

opcao = input("Informe uma opção: ")

if opcao == "1":
    print(1)
elif opcao == "2":
    print(2)
elif opcao == "3":
    print(3)
elif opcao == "4":
    print(4)
elif opcao == "5":
    print(5)
else:
    print("Opção inválida")


#---------------

match opcao: # recuperar a informação da variável
    case "1": # teste caso 1...
        print(1)
    case "2":
        print(2)
    case "3":
        print(3)
    case "4":
        print(4)
    case "5":
        print(5)
    case _:
        print("Opção inválida")
    