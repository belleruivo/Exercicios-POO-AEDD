from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, quantity):
        book = self.find_book(title)
        if book:
            book.quantity += quantity
        else:
            new_book = Book(title, quantity)
            self.books.append(new_book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    # associacao bilateral  
    def make_loan(self, user_name, book_title):
        user = self.find_user(user_name)  # Encontra o usuário pelo nome
        book = self.find_book(book_title)  # Encontra o livro pelo título
        if user and book and book.quantity > 0:  # Verifica se o empréstimo é possível
            loan = Loan(user, book)  # Cria uma nova instância de Loan
            self.loans.append(loan)  # Adiciona o empréstimo à lista de empréstimos
            book.quantity -= 1  # Decrementa a quantidade do livro
            print(f"Livro '{book_title}' emprestado para {user_name}.")
        else:
            print(f"Empréstimo não disponível para o livro '{book_title}'.")

    def find_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def return_book(self, user_name, book_title):
        user = self.find_user(user_name)
        if user:
            for loan in self.loans:
                if loan.user == user and loan.book.title == book_title:
                    self.loans.remove(loan)
                    loan.book.quantity += 1
                    print(f"Livro '{book_title}' devolvido por {user_name}.")
                    return
            print(f"Empréstimo não encontrado para o livro '{book_title}'.")
        else:
            print(f"Usuário {user_name} não encontrado.")
