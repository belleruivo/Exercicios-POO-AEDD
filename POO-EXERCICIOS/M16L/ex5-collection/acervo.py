from abc import ABC, abstractmethod

# Interface para todos os itens de acervo
class ItemAcervo(ABC):
    @abstractmethod
    def descricao(self):
        pass

# Implementações concretas do acervo
class Livro(ItemAcervo):
    def __init__(self, titulo, ano, autor, genero):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

class Revista(ItemAcervo):
    def __init__(self, titulo, ano, editora, edicao):
        self.titulo = titulo
        self.ano = ano
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

class DVD(ItemAcervo):
    def __init__(self, titulo, ano, duracao, diretor):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

class CD(ItemAcervo):
    def __init__(self, titulo, ano, artista, genero):
        self.titulo = titulo
        self.ano = ano
        self.artista = artista
        self.genero = genero

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"