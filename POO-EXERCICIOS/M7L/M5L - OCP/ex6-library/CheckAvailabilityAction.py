from LibraryAction import LibraryAction

class CheckAvailabilityAction(LibraryAction):
    """Ação para verificar a disponibilidade de um livro."""
    def execute(self):
        title = input("Digite o título do livro: ").strip()
        if not title:
            print("O título do livro não pode ser vazio.")
            return
        if self.library.check_availability(title):
            print(f"O livro '{title}' está disponível.")
        else:
            print(f"O livro '{title}' não está disponível.")
