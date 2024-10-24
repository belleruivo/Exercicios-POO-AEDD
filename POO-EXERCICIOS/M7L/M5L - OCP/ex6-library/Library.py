class Library:
    def __init__(self):
        # Inicializa um dicionário para armazenar os livros e suas quantidades
        self.books = {}

    def add_book(self, title, quantity=1):
        """Adiciona um livro à biblioteca."""
        # Verifica se o livro já está no dicionário
        if title in self.books:
            # Se estiver, incrementa a quantidade existente
            self.books[title] += quantity
        else:
            # Se não estiver, adiciona o livro com a quantidade fornecida
            self.books[title] = quantity

    def borrow_book(self, title):
        """Empréstimo de um livro."""
        # Verifica se o livro está disponível e se há pelo menos uma cópia
        if title in self.books and self.books[title] > 0:
            # Decrementa a quantidade do livro
            self.books[title] -= 1
            return True
        # Retorna False se o livro não estiver disponível
        return False

    def return_book(self, title):
        """Devolve um livro para a biblioteca."""
        # Verifica se o livro está no dicionário
        if title in self.books:
            # Incrementa a quantidade do livro
            self.books[title] += 1
        else:
            # Informa que o livro não está cadastrado na biblioteca
            print(f"O livro '{title}' não está cadastrado na biblioteca.")

    def check_availability(self, title):
        """Verifica a disponibilidade de um livro."""
        # Retorna True se o livro estiver disponível, caso contrário, False
        return self.books.get(title, 0) > 0