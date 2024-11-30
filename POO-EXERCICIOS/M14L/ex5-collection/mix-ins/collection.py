class DescricaoMixin:
    def descricao(self):
        atributos = ', '.join(f"{k.capitalize()}: {v}" for k, v in vars(self).items())
        return f"{self.__class__.__name__}: {atributos}"

class Collection:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

class Livro(Collection, DescricaoMixin):
    def __init__(self, titulo, ano, autor, genero):
        super().__init__(titulo, ano)
        self.autor = autor
        self.genero = genero

class Revista(Collection, DescricaoMixin):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao

class DVD(Collection, DescricaoMixin):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.diretor = diretor

class CD(Collection, DescricaoMixin):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        self.artista = artista
        self.genero = genero



