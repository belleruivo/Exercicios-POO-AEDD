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
Composição de Classes: Criamos classes componentes (Curso, Historico, Endereco) que são usadas dentro de Student para compor suas funcionalidades.

Classes Concretas: As classes de estudantes (Graduacao, Especializacao, Mestrado, Doutorado) usam essas classes componentes.

Sistema Interativo: O main.py foi atualizado para incluir a entrada de curso, endereço, e histórico ao adicionar um novo estudante e exibir essas informações ao listar os estudantes.
'''