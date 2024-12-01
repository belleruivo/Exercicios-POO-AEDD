from abc import ABC, abstractmethod

# Base Abstract Class
class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

# Interface for borrowable items
class Borrowable(ABC):
    @abstractmethod
    def emprestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

# Specialized Classes
class Livro(Collection, Borrowable):
    def __init__(self, titulo, ano, autor, genero):
        Collection.__init__(self, titulo, ano)
        self.autor = autor
        self.genero = genero
        self.is_borrowed = False

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

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

class Revista(Collection, Borrowable):
    def __init__(self, titulo, ano, editora, edicao):
        Collection.__init__(self, titulo, ano)
        self.editora = editora
        self.edicao = edicao
        self.is_borrowed = False

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

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

class DVD(Collection, Borrowable):
    def __init__(self, titulo, ano, duracao, diretor):
        Collection.__init__(self, titulo, ano)
        self.duracao = duracao
        self.diretor = diretor
        self.is_borrowed = False

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

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

class CD(Collection, Borrowable):
    def __init__(self, titulo, ano, artista, genero):
        Collection.__init__(self, titulo, ano)
        self.artista = artista
        self.genero = genero
        self.is_borrowed = False

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"

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

# Main function
def criar_acervo():
    while True:
        print("\nSelecione o tipo de acervo:")
        print("1. Livro")
        print("2. Revista")
        print("3. DVD")
        print("4. CD")
        tipo = input("Digite o número correspondente: ").strip()

        if tipo not in {"1", "2", "3", "4"}:
            print("Opção inválida! Por favor, tente novamente.\n")
            continue

        titulo = input("\nTítulo: ").strip()
        while True:
            try:
                ano = int(input("Ano: ").strip())
                break
            except ValueError:
                print("Entrada inválida! O ano deve ser um número. Tente novamente.\n")

        if tipo == "1":
            autor = input("Autor: ").strip()
            genero = input("Gênero: ").strip()
            return Livro(titulo, ano, autor, genero)

        elif tipo == "2":
            editora = input("Editora: ").strip()
            edicao = input("Edição: ").strip()
            return Revista(titulo, ano, editora, edicao)

        elif tipo == "3":
            while True:
                try:
                    duracao = int(input("Duração (em minutos, apenas números): ").strip())
                    break
                except ValueError:
                    print("Entrada inválida! A duração deve ser um número. Tente novamente.\n")
            diretor = input("Diretor: ").strip()
            return DVD(titulo, ano, duracao, diretor)

        elif tipo == "4":
            artista = input("Artista: ").strip()
            genero = input("Gênero: ").strip()
            return CD(titulo, ano, artista, genero)

