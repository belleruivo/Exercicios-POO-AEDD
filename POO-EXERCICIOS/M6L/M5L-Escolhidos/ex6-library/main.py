from biblioteca import Biblioteca

def solicitar_input(prompt, validar_isbn=False):
    while True:
        valor = input(prompt).strip()
        if not valor:
            print("O campo não pode ser vazio.")
        elif validar_isbn and not valor.isdigit():
            print("O ISBN deve ser numérico.")
        else:
            return valor

def cadastrar_livro(biblioteca):
    try:
        titulo = solicitar_input("Digite o título do livro: ")
        autor = solicitar_input("Digite o autor do livro: ")
        isbn = solicitar_input("Digite o ISBN do livro: ", validar_isbn=True)
        categoria = solicitar_input("Digite a categoria do livro: ")

        # Chamada do método para cadastrar livro
        biblioteca.cadastrar_livro(titulo, autor, isbn, categoria)
        print(f"Livro '{titulo}' cadastrado com sucesso.")
        
    except ValueError as e:
        print(f"Erro ao cadastrar livro: {e}")

def cadastrar_usuario(biblioteca):
    try:
        nome = solicitar_input("Digite o nome do usuário: ")
        user_id = solicitar_input("Digite o ID do usuário: ")

        if not user_id.isdigit():
            raise ValueError("O ID do usuário deve ser numérico.")
        
        biblioteca.cadastrar_usuario(nome, int(user_id))
        print(f"Usuário '{nome}' cadastrado com sucesso.")
        
    except ValueError as e:
        print(f"Erro ao cadastrar usuário: {e}")

def fazer_emprestimo(biblioteca):
    try:
        isbn = solicitar_input("Digite o ISBN do livro: ", validar_isbn=True)
        user_id = solicitar_input("Digite o ID do usuário: ")

        if not user_id.isdigit():
            raise ValueError("O ID do usuário deve ser numérico.")

        biblioteca.emprestar_livro(isbn, int(user_id))
        print("Empréstimo realizado com sucesso.")
        
    except ValueError as e:
        print(f"Erro ao fazer empréstimo: {e}")

def devolver_livro(biblioteca):
    try:
        isbn = solicitar_input("Digite o ISBN do livro: ", validar_isbn=True)
        user_id = solicitar_input("Digite o ID do usuário: ")

        if not user_id.isdigit():
            raise ValueError("O ID do usuário deve ser numérico.")

        biblioteca.devolver_livro(isbn, int(user_id))
        print("Devolução realizada com sucesso.")
        
    except ValueError as e:
        print(f"Erro ao devolver livro: {e}")

def verificar_disponibilidade(biblioteca):
    try:
        isbn = solicitar_input("Digite o ISBN do livro: ", validar_isbn=True)

        disponivel = biblioteca.verificar_disponibilidade(isbn)
        if disponivel:
            print(f"O livro com ISBN {isbn} está disponível.")
        else:
            print(f"O livro com ISBN {isbn} não está disponível.")
            
    except ValueError as e:
        print(f"Erro ao verificar disponibilidade: {e}")

def main():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Fazer empréstimo")
        print("4. Devolver livro")
        print("5. Verificar disponibilidade de livro")
        print("6. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            cadastrar_livro(biblioteca)
        elif escolha == '2':
            cadastrar_usuario(biblioteca)
        elif escolha == '3':
            fazer_emprestimo(biblioteca)
        elif escolha == '4':
            devolver_livro(biblioteca)
        elif escolha == '5':
            verificar_disponibilidade(biblioteca)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
