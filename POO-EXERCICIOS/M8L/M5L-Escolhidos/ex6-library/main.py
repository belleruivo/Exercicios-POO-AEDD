from biblioteca import Biblioteca
from bibliotecario import Bibliotecario
from relatorio import Relatorio

def main():
    biblioteca = Biblioteca()
    bibliotecario = Bibliotecario(biblioteca)
    relatorio = Relatorio(biblioteca)

    while True:
        print("\n1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Fazer empréstimo")
        print("4. Devolver livro")
        print("5. Gerar relatório de empréstimos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            titulo = input("Título do livro: ").strip()
            try:
                quantidade = int(input("Quantidade: ").strip())
                bibliotecario.adicionar_livro(titulo, quantidade)
            except ValueError:
                print("Quantidade inválida. Deve ser um número inteiro.")

        elif opcao == '2':
            nome = input("Nome do usuário: ").strip()
            bibliotecario.cadastrar_usuario(nome)

        elif opcao == '3':
            nome_usuario = input("Nome do usuário: ").strip()
            usuario = biblioteca.usuarios.get(nome_usuario)
            titulo_livro = input("Título do livro: ").strip()
            biblioteca.emprestar_livro(usuario, titulo_livro)

        elif opcao == '4':
            nome_usuario = input("Nome do usuário: ").strip()
            usuario = biblioteca.usuarios.get(nome_usuario)
            titulo_livro = input("Título do livro: ").strip()
            biblioteca.devolver_livro(usuario, titulo_livro)

        elif opcao == '5':
            relatorio.gerar_relatorio_emprestimos()

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
