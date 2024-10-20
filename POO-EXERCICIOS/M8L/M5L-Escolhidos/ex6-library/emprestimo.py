from usuario import Usuario
from livro import Livro

class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro

    def efetuar_emprestimo(self):
        return self.usuario.realizar_emprestimo(self.livro)

    def efetuar_devolucao(self):
        return self.usuario.devolver_livro(self.livro)
