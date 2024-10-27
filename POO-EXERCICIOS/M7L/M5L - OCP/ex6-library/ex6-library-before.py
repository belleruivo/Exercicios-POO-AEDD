'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # Indica se o livro está disponível para empréstimo

    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.available})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Adiciona um livro à biblioteca."""
        self.books.append(book)

    def list_books(self):
        """Lista todos os livros na biblioteca."""
        for book in self.books:
            print(book)

    def borrow_book(self, title: str):
        """Realiza o empréstimo de um livro."""
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False  # O livro não está mais disponível
                print(f"You borrowed '{book.title}' by {book.author}.")
                return
        print("Book not available for borrowing.")

    def return_book(self, title: str):
        """Realiza a devolução de um livro."""
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True  # O livro agora está disponível
                print(f"You returned '{book.title}' by {book.author}.")
                return
        print("This book was not borrowed.")

    def check_availability(self, title: str):
        """Verifica a disponibilidade de um livro."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    print(f"The book '{book.title}' is available.")
                else:
                    print(f"The book '{book.title}' is currently not available.")
                return
        print("Book not found in the library.")


def main():
    library = Library()

    while True:
        action = input("Choose action (add, borrow, return, check, list, exit): ").strip().lower()

        if action == "add":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(Book(title, author))
            print(f"Added '{title}' by {author}.")

        elif action == "list":
            print("Books in the library:")
            library.list_books()

        elif action == "borrow":
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)

        elif action == "return":
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)

        elif action == "check":
            title = input("Enter the title of the book to check availability: ")
            library.check_availability(title)

        elif action == "exit":
            print("Exiting the library system.")
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
