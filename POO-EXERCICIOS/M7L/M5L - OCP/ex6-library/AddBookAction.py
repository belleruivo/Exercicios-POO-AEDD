from LibraryAction import LibraryAction

class AddBookAction(LibraryAction):
    """Ação para adicionar um livro na biblioteca."""
    def execute(self):
        title = input("Digite o título do livro: ").strip()
        if not title:
            print("O título do livro não pode ser vazio.")
            return
        try:
            quantity = int(input("Digite a quantidade: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Quantidade inválida. Deve ser um número inteiro positivo.")
            return
        self.library.add_book(title, quantity)
        print(f"Livro '{title}' cadastrado com sucesso!")
