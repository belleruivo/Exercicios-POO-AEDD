class Usuario:
    def __init__(self, nome, user_id):
        if not nome or not isinstance(user_id, int):
            raise ValueError("Nome do usuário e ID (numérico) são obrigatórios.")
        self.nome = nome
        self.user_id = user_id
        self.livros_emprestados = []

    def adicionar_emprestimo(self, emprestimo):
        self.livros_emprestados.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self.livros_emprestados.remove(emprestimo)

    def __repr__(self):
        return f"Usuario(nome={self.nome}, user_id={self.user_id}, livros_emprestados={self.livros_emprestados})"
