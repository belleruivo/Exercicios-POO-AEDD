class Categoria:
    def __init__(self, nome):
        if not nome:
            raise ValueError("Nome da categoria é obrigatório.")
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def __repr__(self):
        return f"Categoria(nome={self.nome}, livros={[livro.titulo for livro in self.livros]})"
