class Categoria:
    def __init__(self, nome):
        # inicializa a classe categoria com nome e uma lista vazia de livros
        if not nome:
            # verifica se o nome é fornecido, caso contrário, lança um erro
            raise ValueError("Nome da categoria é obrigatório.")
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        # adiciona um livro à lista de livros da categoria
        self.livros.append(livro)

    def listar_livros(self):
        # retorna a lista de livros da categoria
        return self.livros

    def __repr__(self):
        # retorna uma representação string da categoria, incluindo o nome e os títulos dos livros
        return f"Categoria(nome={self.nome}, livros={[livro.titulo for livro in self.livros]})"