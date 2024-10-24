class Catalogo:
    def __init__(self):
        # inicializa a classe catalogo com uma lista vazia de livros
        self.livros = []

    def adicionar_livro(self, livro):
        # adiciona um livro à lista de livros do catálogo
        self.livros.append(livro)

    def remover_livro(self, livro):
        # remove um livro da lista de livros do catálogo
        self.livros.remove(livro)

    def buscar_livro(self, isbn):
        # busca um livro pelo isbn na lista de livros do catálogo
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def __repr__(self):
        # retorna uma representação string do catálogo, incluindo a lista de livros
        return f"Catalogo(livros={self.livros})"