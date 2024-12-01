from abc import ABC, abstractmethod

# Base Abstract Class
class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

# Mix-In for borrowable items
class Borrowable:
    def __init__(self):
        self.is_borrowed = False

    def emprestar(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"'{self.titulo}' foi emprestado com sucesso!"
        else:
            return f"'{self.titulo}' já está emprestado!"

    def devolver(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"'{self.titulo}' foi devolvido com sucesso!"
        else:
            return f"'{self.titulo}' não estava emprestado!"

# Specialized Classes
class Livro(Collection, Borrowable):
    def __init__(self, titulo, ano, autor, genero):
        Collection.__init__(self, titulo, ano)
        Borrowable.__init__(self)
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

class Revista(Collection, Borrowable):
    def __init__(self, titulo, ano, editora, edicao):
        Collection.__init__(self, titulo, ano)
        Borrowable.__init__(self)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

class DVD(Collection, Borrowable):
    def __init__(self, titulo, ano, duracao, diretor):
        Collection.__init__(self, titulo, ano)
        Borrowable.__init__(self)
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

class CD(Collection, Borrowable):
    def __init__(self, titulo, ano, artista, genero):
        Collection.__init__(self, titulo, ano)
        Borrowable.__init__(self)
        self.artista = artista
        self.genero = genero

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"

