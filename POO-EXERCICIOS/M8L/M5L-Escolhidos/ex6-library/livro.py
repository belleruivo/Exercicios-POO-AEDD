class Livro:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def emprestar(self):
        if self.quantidade > 0:
            self.quantidade -= 1
            return True
        return False

    def devolver(self):
        self.quantidade += 1

    def disponivel(self):
        return self.quantidade > 0
