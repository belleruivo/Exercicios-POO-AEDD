# main.py
from aluno import PilhaAlunos
from nota import FilaNotas

def calcular_media(aluno):
    if not aluno.notas:
        return "Aluno sem notas."
    media = sum(aluno.notas) / len(aluno.notas)
    return f"Média do aluno = {media:.2f}"

def menu():
    pilha_alunos = PilhaAlunos()
    fila_notas = FilaNotas()

    while True:
        print("\nMENU")
        print("1- Cadastrar aluno")
        print("2- Cadastrar nota")
        print("3- Calcular média de um aluno")
        print("4- Listar os nomes dos alunos sem notas")
        print("5- Excluir aluno")
        print("6- Excluir nota")
        print("7- Sair")

        opcao = input("Escolha uma opção: ").strip()
        if not opcao.isdigit() or int(opcao) < 1 or int(opcao) > 7:
            print("Opção inválida. Escolha uma opção entre 1 e 7.")
            continue

        if opcao == "1":
            nome = input("Digite o nome do aluno: ").strip()
            print(pilha_alunos.cadastrar_aluno(nome))

        elif opcao == "2":
            numero_aluno = input("Digite o número do aluno: ").strip()
            valor_nota = input("Digite a nota: ").strip()
            print(fila_notas.cadastrar_nota(numero_aluno, valor_nota, pilha_alunos))

        elif opcao == "3":
            numero_aluno = input("Digite o número do aluno: ").strip()
            aluno = pilha_alunos.obter_aluno(numero_aluno)
            if aluno is None:
                print("Aluno não cadastrado.")
            else:
                print(f"Nome do aluno: {aluno.nome}")
                print(calcular_media(aluno))

        elif opcao == "4":
            print(pilha_alunos.listar_alunos_sem_nota())

        elif opcao == "5":
            print(pilha_alunos.excluir_aluno())

        elif opcao == "6":
            print(fila_notas.excluir_nota())

        elif opcao == "7":
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    menu()
