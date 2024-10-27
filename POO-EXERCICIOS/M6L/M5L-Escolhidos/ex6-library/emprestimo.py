from datetime import datetime

class Emprestimo:
    def __init__(self, livro, usuario):
        # inicializa a classe emprestimo com livro, usuario, data de emprestimo e data de devolucao
        if not livro or not usuario:
            # verifica se o livro e o usuario são fornecidos, caso contrário, lança um erro
            raise ValueError("Livro e Usuário são obrigatórios para o empréstimo.")
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def registrar_devolucao(self):
        # registra a data de devolução do livro
        self.data_devolucao = datetime.now()

    def __repr__(self):
        # retorna uma representação string do emprestimo, incluindo o livro, usuario, data de emprestimo e data de devolucao
        return f"Emprestimo(livro={self.livro.titulo}, usuario={self.usuario.nome}, data_emprestimo={self.data_emprestimo}, data_devolucao={self.data_devolucao})"