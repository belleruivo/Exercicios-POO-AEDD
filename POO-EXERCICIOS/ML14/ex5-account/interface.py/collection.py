from abc import ABC, abstractmethod

class ItemAcervo(ABC):
    @abstractmethod
    def descricao(self):
        pass

class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

class Livro(Collection, ItemAcervo):
    def __init__(self, titulo, ano, autor, genero):
        super().__init__(titulo, ano)
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

class Revista(Collection, ItemAcervo):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

class DVD(Collection, ItemAcervo):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

class CD(Collection, ItemAcervo):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        self.artista = artista
        self.genero = genero

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"
