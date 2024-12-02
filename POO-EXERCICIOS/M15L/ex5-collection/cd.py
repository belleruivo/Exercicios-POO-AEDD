from collection import Collection

class CD(Collection):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        self.artista = artista
        self.genero = genero
        self.is_borrowed = False

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"
