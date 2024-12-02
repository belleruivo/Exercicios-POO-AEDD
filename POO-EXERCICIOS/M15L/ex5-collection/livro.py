from collection import Collection
from borrowableMixin import BorrowableMixin

class Livro(Collection, BorrowableMixin):
    def __init__(self, titulo, ano, autor, genero):
        Collection.__init__(self, titulo, ano)
        BorrowableMixin.__init__(self)
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"
