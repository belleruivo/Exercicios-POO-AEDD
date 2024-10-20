from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}

    def adicionar_livro(self, titulo, quantidade=1):
        if titulo in self.livros:
            self.livros[titulo].quantidade += quantidade
        else:
            self.livros[titulo] = Livro(titulo, quantidade)
        print(f"Livro '{titulo}' adicionado/atualizado com sucesso!")

    def cadastrar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = Usuario(nome)
            print(f"Usuário '{nome}' cadastrado com sucesso!")
        else:
            print(f"Usuário '{nome}' já está cadastrado.")

    def emprestar_livro(self, usuario: Usuario, titulo_livro: str):
        livro = self.livros.get(titulo_livro)
        if usuario and livro:
            emprestimo = Emprestimo(usuario, livro)
            emprestimo.efetuar_emprestimo()
        else:
            print("Usuário ou livro não encontrados.")

    def devolver_livro(self, usuario: Usuario, titulo_livro: str):
        livro = self.livros.get(titulo_livro)
        if usuario and livro:
            emprestimo = Emprestimo(usuario, livro)
            emprestimo.efetuar_devolucao()
        else:
            print("Usuário ou livro não encontrados.")
