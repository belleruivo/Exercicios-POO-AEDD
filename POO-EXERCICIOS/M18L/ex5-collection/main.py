from abc import ABC, abstractmethod

class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

class Livro(Collection):
    def __init__(self, titulo, ano, autor, genero):
        super().__init__(titulo, ano)
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

class Revista(Collection):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

class DVD(Collection):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

class CD(Collection):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        self.artista = artista
        self.genero = genero

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"

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

        titulo = input("Título: ").strip()
        
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

def main():
    acervo = []
    while True:
        item = criar_acervo()
        if item:
            acervo.append(item)
            print("Item adicionado com sucesso!\n")
        
        while True:
            continuar = input("Deseja adicionar outro item? (s/n): ").strip().lower()
            print()
            if continuar in {"s", "n"}:
                break
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.\n")
        
        if continuar == "n":
            break
    
    print("Acervo da Biblioteca:")
    for item in acervo:
        print(item.descricao())

main()
