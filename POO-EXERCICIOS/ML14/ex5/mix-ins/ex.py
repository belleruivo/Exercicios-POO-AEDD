from abc import ABC, abstractmethod

# Mix-in para adicionar funcionalidade de disponibilidade
class DisponibilidadeMixin:
    def __init__(self):
        self.disponivel = True  # Inicia como disponível
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"O item '{self.titulo}' foi emprestado com sucesso!"
        else:
            return f"O item '{self.titulo}' não está disponível para empréstimo."
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return f"O item '{self.titulo}' foi devolvido com sucesso!"
        else:
            return f"O item '{self.titulo}' já está disponível."

class Collection(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

class Livro(Collection, DisponibilidadeMixin):
    def __init__(self, titulo, ano, autor, genero):
        super().__init__(titulo, ano)
        DisponibilidadeMixin.__init__(self)  # Inicializa o mix-in
        self.autor = autor
        self.genero = genero

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Ano: {self.ano}"

class Revista(Collection, DisponibilidadeMixin):
    def __init__(self, titulo, ano, editora, edicao):
        super().__init__(titulo, ano)
        DisponibilidadeMixin.__init__(self)  # Inicializa o mix-in
        self.editora = editora
        self.edicao = edicao

    def descricao(self):
        return f"Revista: {self.titulo}, Editora: {self.editora}, Edição: {self.edicao}, Ano: {self.ano}"

class DVD(Collection, DisponibilidadeMixin):
    def __init__(self, titulo, ano, duracao, diretor):
        super().__init__(titulo, ano)
        DisponibilidadeMixin.__init__(self)  # Inicializa o mix-in
        self.duracao = duracao
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo}, Diretor: {self.diretor}, Duração: {self.duracao} min, Ano: {self.ano}"

class CD(Collection, DisponibilidadeMixin):
    def __init__(self, titulo, ano, artista, genero):
        super().__init__(titulo, ano)
        DisponibilidadeMixin.__init__(self)  # Inicializa o mix-in
        self.artista = artista
        self.genero = genero

    def descricao(self):
        return f"CD: {self.titulo}, Artista: {self.artista}, Gênero: {self.genero}, Ano: {self.ano}"

# Função de criação do acervo
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
                ano = int(input("Ano (apenas números): ").strip())
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

# Função principal
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

    # Exemplo de uso do mix-in
    print("\nTestando funcionalidades de disponibilidade:")
    for item in acervo:
        print(item.emprestar())  # Tenta emprestar o item
        print(item.devolver())   # Tenta devolver o item

main()