class Autor:
    def __init__(self, nome):
        # inicializa a classe autor com nome e uma lista vazia de livros
        if not nome:
            raise ValueError("Nome do autor é obrigatório.")
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        # adiciona um livro à lista de livros do autor (na posição final)
        self.livros.append(livro)

    def listar_livros(self):
        # retorna a lista de livros do autor
        return self.livros

    def __repr__(self):
        # retorna uma representação string do autor, incluindo o nome e os títulos dos livros
        return f"Autor(nome={self.nome}, livros={[livro.titulo for livro in self.livros]})"