from abc import ABC, abstractmethod

class DescricaoMixin:
    def descricao(self):
        return f"{self.__class__.__name__}: {self.titulo}, Ano: {self.ano}"

class AnoMixin:
    def get_ano(self):
        return f"Ano de lançamento: {self.ano}"

class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

class Livro(Collection, DescricaoMixin, AnoMixin):
    def __init__(self, titulo, ano, autor, genero):
        Collection.__init__(self, titulo, ano)
        self.autor = autor
        self.genero = genero

    def descricao(self):
        descricao_base = DescricaoMixin.descricao(self)
        ano = AnoMixin.get_ano(self)  
        return f"{descricao_base}, Autor: {self.autor}, Gênero: {self.genero}, {ano}"

class Revista(Collection, DescricaoMixin, AnoMixin):
    def __init__(self, titulo, ano, editora, edicao):
        Collection.__init__(self, titulo, ano)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        descricao_base = DescricaoMixin.descricao(self)
        ano = AnoMixin.get_ano(self)  
        return f"{descricao_base}, Editora: {self.editora}, Edição: {self.edicao}, {ano}"

class DVD(Collection, DescricaoMixin, AnoMixin):
    def __init__(self, titulo, ano, duracao, diretor):
        Collection.__init__(self, titulo, ano)
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        descricao_base = DescricaoMixin.descricao(self)
        ano = AnoMixin.get_ano(self)
        return f"{descricao_base}, Diretor: {self.diretor}, Duração: {self.duracao} min, {ano}"

class CD(Collection, DescricaoMixin, AnoMixin):
    def __init__(self, titulo, ano, artista, genero):
        Collection.__init__(self, titulo, ano)
        self.artista = artista
        self.genero = genero

    def descricao(self):
        descricao_base = DescricaoMixin.descricao(self)
        ano = AnoMixin.get_ano(self)  
        return f"{descricao_base}, Artista: {self.artista}, Gênero: {self.genero}, {ano}"

