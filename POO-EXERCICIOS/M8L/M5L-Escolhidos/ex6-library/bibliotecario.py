from biblioteca import Biblioteca

class Bibliotecario:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def adicionar_livro(self, titulo, quantidade):
        self.biblioteca.adicionar_livro(titulo, quantidade)

    def cadastrar_usuario(self, nome):
        self.biblioteca.cadastrar_usuario(nome)

# Injeção de Dependência:
# A classe Bibliotecario recebe uma instância de Biblioteca através de seu construtor. Isso permite que a classe Bibliotecario utilize a funcionalidade da Biblioteca sem criar uma nova instância dela. Isso facilita a substituição da implementação da biblioteca (por exemplo, em testes) e reduz o acoplamento.