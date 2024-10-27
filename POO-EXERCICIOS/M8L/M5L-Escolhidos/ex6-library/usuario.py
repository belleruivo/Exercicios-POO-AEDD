class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def realizar_emprestimo(self, livro):
        if livro.emprestar():
            self.emprestimos.append(livro.titulo)
            print(f"Empréstimo do livro '{livro.titulo}' realizado para {self.nome}!")
            return True
        print(f"Livro '{livro.titulo}' não disponível para empréstimo.")
        return False

    def devolver_livro(self, livro):
        if livro.titulo in self.emprestimos:
            livro.devolver()
            self.emprestimos.remove(livro.titulo)
            print(f"{self.nome} devolveu o livro '{livro.titulo}' com sucesso!")
            return True
        print(f"{self.nome} não tem o livro '{livro.titulo}' para devolver.")
        return False
