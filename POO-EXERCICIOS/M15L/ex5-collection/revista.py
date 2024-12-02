from collection import Collection
class Revista(Collection):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao
        self.is_borrowed = False

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"