print("""
    [PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos 
             e seus números de matrícula usando um dicionário.

    O programa deve fornecer as seguintes funcionalidades:
    Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
    Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
    Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, 
    exibindo seus respectivos números de matrícula.
    
    O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
""")

alunos = {}

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")

def remover_aluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def visualizar_alunos():
    print("Lista de alunos:")
    for matricula, nome in alunos.items():
        print(f"Matrícula: {matricula} - Nome: {nome}")

def main():
    while True:
        print('#---------------------------------#')
        print("\nEscolha uma opção:")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Visualizar todos os alunos")
        print("4. Sair")
        print('#---------------------------------#')
        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            remover_aluno()
        elif opcao == "3":
            visualizar_alunos()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
