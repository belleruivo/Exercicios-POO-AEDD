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

# Injeção de Dependência:
# A classe Emprestimo recebe instâncias de Usuario e Livro em seu construtor. Isso torna o Emprestimo mais flexível, pois pode trabalhar com diferentes usuários e livros sem depender de instâncias fixas. Esse design permite também a criação de testes onde você pode simular diferentes cenários de empréstimos.