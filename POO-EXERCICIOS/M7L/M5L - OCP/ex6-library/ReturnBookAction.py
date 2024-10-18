from LibraryAction import LibraryAction

class ReturnBookAction(LibraryAction):
    """Ação para devolver um livro."""
    def execute(self):
        title = input("Digite o título do livro: ").strip()
        if not title:
            print("O título do livro não pode ser vazio.")
            return
        self.library.return_book(title)
        print(f"Livro '{title}' devolvido com sucesso!")
