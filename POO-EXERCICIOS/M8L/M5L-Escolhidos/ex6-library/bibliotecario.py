from biblioteca import Biblioteca

class Bibliotecario:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def adicionar_livro(self, titulo, quantidade):
        self.biblioteca.adicionar_livro(titulo, quantidade)

    def cadastrar_usuario(self, nome):
        self.biblioteca.cadastrar_usuario(nome)
