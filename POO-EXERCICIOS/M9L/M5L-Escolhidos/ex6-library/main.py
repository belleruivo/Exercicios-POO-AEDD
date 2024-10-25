'''Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência.'''

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


# Análise da Associação Bilateral
# A associação bilateral é claramente demonstrada entre as classes Loan, User e Book:

# Loan: Esta classe contém referências a um objeto User e a um objeto Book:

# self.user = user: Referencia o usuário que fez o empréstimo.
# self.book = book: Referencia o livro que foi emprestado.
# Essa estrutura de dados cria uma associação entre os empréstimos e os usuários e livros envolvidos.

# Library: A classe Library é responsável por gerenciar as instâncias de User, Book e Loan. Quando um empréstimo é criado através do método make_loan, a biblioteca referencia tanto o usuário quanto o livro:

# loan = Loan(user, book): Cria um novo empréstimo que associa o User e o Book.
# User: A classe User tem um atributo que define seu nome, mas não mantém uma referência direta a empréstimos. Contudo, a interação entre o usuário e o livro ocorre na classe Loan.

# Considerações sobre a Associação Bilateral
# A implementação atual já reflete uma associação bilateral entre as classes de forma eficaz. Vamos resumi-las:

# Entre Loan e User: Cada Loan tem um User, permitindo que se acesse as informações do usuário associado ao empréstimo.
# Entre Loan e Book: Cada Loan tem um Book, permitindo que se acesse as informações do livro emprestado.