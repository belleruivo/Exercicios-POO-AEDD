'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

class ExtendedLibrary(Library):
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

def main():
    library = ExtendedLibrary()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    library.list_books()

    found_book = library.find_book_by_title("1984")
    if found_book:
        print(f"Found book: {found_book}")
    else:
        print("Book not found")

if __name__ == "__main__":
    main()