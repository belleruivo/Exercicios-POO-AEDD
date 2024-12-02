from abc import ABC, abstractmethod

# Base Abstract Class for Collection Items
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

# Livro implementation
class Livro(Collection):
    def __init__(self, titulo, ano, autor, genero):
        super().__init__(titulo, ano)
        self.autor = autor
        self.genero = genero
        self.is_borrowed = False

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

# Register Livro as a Borrowable subclass
Borrowable.register(Livro)

# Add Borrowable functionality to Livro
def livro_emprestar(self):
    if not self.is_borrowed:
        self.is_borrowed = True
        return f"'{self.titulo}' foi emprestado com sucesso!"
    else:
        return f"'{self.titulo}' já está emprestado!"

def livro_devolver(self):
    if self.is_borrowed:
        self.is_borrowed = False
        return f"'{self.titulo}' foi devolvido com sucesso!"
    else:
        return f"'{self.titulo}' não estava emprestado!"

Livro.emprestar = livro_emprestar
Livro.devolver = livro_devolver

# Similar implementations for Revista, DVD, and CD
class Revista(Collection):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        self.editora = editora
        self.edicao = edicao
        self.is_borrowed = False

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

Borrowable.register(Revista)

Revista.emprestar = livro_emprestar
Revista.devolver = livro_devolver

class DVD(Collection):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.diretor = diretor
        self.is_borrowed = False

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

Borrowable.register(DVD)

DVD.emprestar = livro_emprestar
DVD.devolver = livro_devolver

class CD(Collection):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        self.artista = artista
        self.genero = genero
        self.is_borrowed = False

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"

Borrowable.register(CD)

CD.emprestar = livro_emprestar
CD.devolver = livro_devolver

# Main function remains similar, but logic ensures interface checks
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

def main():
    acervo = []
    while True:
        print("\nSelecione uma ação:")
        print("1. Adicionar Item")
        print("2. Emprestar Item")
        escolha = input("Digite o número correspondente: ").strip()

        if escolha == "1":
            item = criar_acervo()
            if item:
                acervo.append(item)
                print("Item adicionado com sucesso!\n")

        elif escolha == "2":
            if not acervo:
                print("O acervo está vazio! Adicione um item primeiro.\n")
                continue
            
            print("\nItens do acervo disponíveis para empréstimo:")
            for idx, item in enumerate(acervo, 1):
                print(f"{idx}. {item.descricao()}")
            
            while True:
                try:
                    escolha_item = int(input("\nEscolha o número do item que deseja emprestar: ").strip())
                    if 1 <= escolha_item <= len(acervo):
                        item = acervo[escolha_item - 1]
                        if isinstance(item, Borrowable):  # Verifica se o item pode ser emprestado
                            print(item.emprestar())
                        else:
                            print(f"'{item.titulo}' não pode ser emprestado!")
                        break
                    else:
                        print("Número inválido. Tente novamente.\n")
                except ValueError:
                    print("Entrada inválida! Digite um número.\n")
        else:
            print("Opção inválida! Tente novamente.")

        while True:
            continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
            if continuar in {"s", "n"}:
                break
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.\n")
        
        if continuar == "n":
            break

main()

