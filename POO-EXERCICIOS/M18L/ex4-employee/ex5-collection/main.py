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

class Emprestimo:
    def __init__(self, item, usuario):
        if not isinstance(item, Collection):
            raise TypeError("O item deve ser uma instância de Collection.")
        self.item = item
        self.usuario = usuario

    def descricao(self):
        return (f"Empréstimo:\n"
                f"Usuário: {self.usuario}\n"
                f"Item: {self.item.descricao()}")

def criar_acervo():
    print("\nSelecione o tipo de acervo:")
    print("1. Livro")
    print("2. Revista")
    print("3. DVD")
    print("4. CD")
    tipo = input("Digite o número correspondente: ").strip()

    if tipo not in {"1", "2", "3", "4"}:
        print("Opção inválida!")
        return None

    titulo = input("Título: ").strip()
    while True:
        try:
            ano = int(input("Ano: ").strip())
            break
        except ValueError:
            print("Entrada inválida! O ano deve ser um número.")

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
                duracao = int(input("Duração (em minutos): ").strip())
                break
            except ValueError:
                print("Entrada inválida! A duração deve ser um número.")
        diretor = input("Diretor: ").strip()
        return DVD(titulo, ano, duracao, diretor)
    elif tipo == "4": 
        artista = input("Artista: ").strip()
        genero = input("Gênero: ").strip()
        return CD(titulo, ano, artista, genero)

def main():
    acervo = []
    emprestimos = []

    while True:
        print("\nMenu Principal")
        print("1. Adicionar item ao acervo")
        print("2. Realizar empréstimo")
        print("3. Listar acervo")
        print("4. Listar empréstimos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            item = criar_acervo()
            if item:
                acervo.append(item)
                print("Item adicionado com sucesso!")
        elif opcao == "2":
            if not acervo:
                print("O acervo está vazio! Adicione itens antes de realizar um empréstimo.")
                continue
            print("\nItens disponíveis para empréstimo:")
            for i, item in enumerate(acervo, 1):
                print(f"{i}. {item.descricao()}")
            while True:
                try:
                    escolha = int(input("\nSelecione o item pelo número: ").strip()) - 1
                    if 0 <= escolha < len(acervo):
                        usuario = input("Nome do usuário: ").strip()
                        emprestimo = Emprestimo(acervo[escolha], usuario)
                        emprestimos.append(emprestimo)
                        print("Empréstimo realizado com sucesso!")
                        break
                    else:
                        print("Número inválido!")
                except ValueError:
                    print("Entrada inválida!")
        elif opcao == "3":
            print("Itens no acervo:")
            for item in acervo:
                print(item.descricao())
        elif opcao == "4":
            print("Empréstimos realizados:")
            for emprestimo in emprestimos:
                print(emprestimo.descricao())
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida!")
main()