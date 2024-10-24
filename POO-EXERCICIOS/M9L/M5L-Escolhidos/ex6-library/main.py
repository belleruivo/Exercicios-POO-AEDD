from library import Library

def main():
    library = Library()

    while True:
        print("\n1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Fazer empréstimo")
        print("4. Devolver livro")
        print("5. Sair")

        option = input("Escolha uma opção: ")

        if option == '1':
            title = input("Digite o título do livro: ")
            quantity = int(input("Digite a quantidade: "))
            library.add_book(title, quantity)

        elif option == '2':
            name = input("Digite o nome do usuário: ")
            library.register_user(name)

        elif option == '3':
            user_name = input("Digite o nome do usuário: ")
            book_title = input("Digite o título do livro: ")
            library.make_loan(user_name, book_title)

        elif option == '4':
            user_name = input("Digite o nome do usuário: ")
            book_title = input("Digite o título do livro: ")
            library.return_book(user_name, book_title)

        elif option == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
