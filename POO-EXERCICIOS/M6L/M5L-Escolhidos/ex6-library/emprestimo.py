from datetime import datetime

class Emprestimo:
    def __init__(self, livro, usuario):
        if not livro or not usuario:
            raise ValueError("Livro e Usuário são obrigatórios para o empréstimo.")
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def registrar_devolucao(self):
        self.data_devolucao = datetime.now()

    def __repr__(self):
        return f"Emprestimo(livro={self.livro.titulo}, usuario={self.usuario.nome}, data_emprestimo={self.data_emprestimo}, data_devolucao={self.data_devolucao})"
