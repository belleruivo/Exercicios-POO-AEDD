class Catalogo:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def __repr__(self):
        # retorna uma representação string do catálogo, incluindo a lista de livros
        return f"Catalogo(livros={self.livros})"