from adicionar_estudante import *

def main():
    estudantes = []
    
    while True:
        print("\nSistema de Gestão Acadêmica")
        print("1. Adicionar Estudante")
        print("2. Listar Estudantes")
        print("3. Sair")
        
        opcao = int(input("Selecione uma opção (1-3): "))
        
        if opcao == 1:
            adicionar_estudante(estudantes)
        elif opcao == 2:
            listar_estudantes(estudantes)
        elif opcao == 3:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''
Composição: A composição é uma relação de "todo-parte" onde o objeto "todo" (Student) é composto por objetos "parte" (Curso, Endereco, Historico).
'''