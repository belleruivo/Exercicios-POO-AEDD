class Library:
    def __init__(self):
        self.books = {}  # Dicionário para armazenar os livros e suas quantidades

    def add_book(self, title, quantity=1):
        """Adiciona um livro à biblioteca."""
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity

    def borrow_book(self, title):
        """Empréstimo de um livro."""
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            return True
        return False

    def return_book(self, title):
        """Devolve um livro para a biblioteca."""
        if title in self.books:
            self.books[title] += 1
        else:
            print(f"O livro '{title}' não está cadastrado na biblioteca.")

    def check_availability(self, title):
        """Verifica a disponibilidade de um livro."""
        return self.books.get(title, 0) > 0
