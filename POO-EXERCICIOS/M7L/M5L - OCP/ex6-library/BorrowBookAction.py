from LibraryAction import LibraryAction

class BorrowBookAction(LibraryAction):
    def execute(self):
        title = input("Digite o título do livro: ").strip()
        if not title:
            print("O título do livro não pode ser vazio.")
            return
        if self.library.borrow_book(title):
            print(f"Empréstimo do livro '{title}' realizado com sucesso!")
        else:
            print(f"Livro '{title}' não disponível para empréstimo.")
