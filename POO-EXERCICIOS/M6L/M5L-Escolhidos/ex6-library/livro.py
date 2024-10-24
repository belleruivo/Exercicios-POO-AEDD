class Livro:
    def __init__(self, titulo, autor, isbn, categoria):
        # inicializa a classe livro com titulo, autor, isbn, disponibilidade e categoria
        if not titulo or not isbn:
            # verifica se o titulo e o isbn são fornecidos, caso contrário, lança um erro
            raise ValueError("Título e ISBN do livro são obrigatórios.")
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True
        self.categoria = categoria

    def alterar_disponibilidade(self, status):
        # altera o status de disponibilidade do livro
        self.disponivel = status

    def __repr__(self):
        # retorna uma representação string do livro, incluindo o titulo, autor, isbn, disponibilidade e categoria
        return f"Livro(titulo={self.titulo}, autor={self.autor}, isbn={self.isbn}, disponivel={self.disponivel}, categoria={self.categoria})"