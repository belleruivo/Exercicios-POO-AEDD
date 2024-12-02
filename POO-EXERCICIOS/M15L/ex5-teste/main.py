from abc import ABC, abstractmethod

# Base Abstract Class for Collection Items
class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

class Borrowable(ABC):
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
                status = "Disponível" if isinstance(item, Borrowable) and not item.is_borrowed else "Indisponível"
                print(f"{idx}. {item.descricao()} - [{status}]")
            
            while True:
                try:
                    escolha_item = int(input("\nEscolha o número do item que deseja emprestar (ou 0 para cancelar): ").strip())
                    if escolha_item == 0:
                        print("Operação de empréstimo cancelada.\n")
                        break

                    if 1 <= escolha_item <= len(acervo):
                        item = acervo[escolha_item - 1]
                        if isinstance(item, Borrowable):
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

main()
