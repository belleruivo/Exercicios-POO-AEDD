class Usuario:
    def __init__(self, nome, user_id):
        # inicializa a classe usuario com nome, user_id e uma lista vazia de livros emprestados
        if not nome or not isinstance(user_id, int):
            # verifica se o nome é fornecido e se o user_id é um inteiro, caso contrário, lança um erro
            raise ValueError("Nome do usuário e ID (numérico) são obrigatórios.")
        self.nome = nome
        self.user_id = user_id
        self.livros_emprestados = []

    def adicionar_emprestimo(self, emprestimo):
        # adiciona um empréstimo à lista de livros emprestados do usuário
        self.livros_emprestados.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        # remove um empréstimo da lista de livros emprestados do usuário
        self.livros_emprestados.remove(emprestimo)

    def __repr__(self):
        # retorna uma representação string do usuário, incluindo o nome, user_id e os livros emprestados
        return f"Usuario(nome={self.nome}, user_id={self.user_id}, livros_emprestados={self.livros_emprestados})"