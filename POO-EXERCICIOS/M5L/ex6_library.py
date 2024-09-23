'''
Em todos os exercícios abaixo, identifique a possibilidade de usar além dos métodos de
objetos, métodos de classe (@classmethod) e métodos fora de contexto (@staticmethod).

6. implemente uma classe chamada library que represente uma biblioteca virtual. essa
classe deve permitir cadastrar livros, fazer empréstimos, devolver livros e verificar a
disponibilidade de um livro.
'''

class Library:
    def __init__(self):  # inicializa a classe library
        self.books = {}  # dicionário para armazenar os livros e suas quantidades

    def add_book(self, title, quantity=1):  # método para adicionar livros
        if title in self.books:  # se o livro já estiver no dicionário
            self.books[title] += quantity  # incrementa a quantidade existente
        else:
            self.books[title] = quantity  # adiciona o livro com a quantidade especificada

    def borrow_book(self, title):  # método para emprestar um livro
        if title in self.books and self.books[title] > 0:  # verifica se o livro está disponível
            self.books[title] -= 1  # decrementa a quantidade do livro
            return True  # retorna true se o empréstimo for bem-sucedido
        return False  # retorna false se o livro não estiver disponível

    def return_book(self, title):  # método para devolver um livro
        if title in self.books:  # verifica se o livro está cadastrado
            self.books[title] += 1  # incrementa a quantidade do livro
        else:
            print(f"livro '{title}' não está cadastrado na biblioteca.")  # mensagem de erro se o livro não estiver cadastrado

    def check_availability(self, title):  # método para verificar a disponibilidade de um livro
        return self.books.get(title, 0) > 0  # retorna true se o livro estiver disponível, caso contrário, false

def main():
    library = Library()  # cria uma instância da classe library
    
    while True:
        print("\n1. cadastrar livro")
        print("2. fazer empréstimo")
        print("3. devolver livro")
        print("4. verificar disponibilidade")
        print("5. sair")
        
        choice = input("escolha uma opção: ")  # solicita ao usuário que escolha uma opção
        
        if choice == '1':  # opção para cadastrar um livro
            title = input("digite o título do livro: ").strip()  # solicita o título do livro
            if not title:  # verifica se o título não está vazio
                print("o título do livro não pode ser vazio.")
                continue
            try:
                quantity = int(input("digite a quantidade: "))  # solicita a quantidade do livro
                if quantity <= 0:  # verifica se a quantidade é um número inteiro positivo
                    raise ValueError
            except ValueError:
                print("quantidade inválida. deve ser um número inteiro positivo.")
                continue
            library.add_book(title, quantity)  # adiciona o livro à biblioteca
            print(f"livro '{title}' cadastrado com sucesso!")
        
        elif choice == '2':  # opção para fazer empréstimo de um livro
            title = input("digite o título do livro: ").strip()  # solicita o título do livro
            if not title:  # verifica se o título não está vazio
                print("o título do livro não pode ser vazio.")
                continue
            if library.borrow_book(title):  # tenta emprestar o livro
                print(f"empréstimo do livro '{title}' realizado com sucesso!")
            else:
                print(f"livro '{title}' não disponível para empréstimo.")
        
        elif choice == '3':  # opção para devolver um livro
            title = input("digite o título do livro: ").strip()  # solicita o título do livro
            if not title:  # verifica se o título não está vazio
                print("o título do livro não pode ser vazio.")
                continue
            if title in library.books:  # verifica se o livro está cadastrado
                library.return_book(title)  # devolve o livro
                print(f"livro '{title}' devolvido com sucesso!")
            else:
                print(f"livro '{title}' não está cadastrado na biblioteca.")
        
        elif choice == '4':  # opção para verificar a disponibilidade de um livro
            title = input("digite o título do livro: ").strip()  # solicita o título do livro
            if not title:  # verifica se o título não está vazio
                print("o título do livro não pode ser vazio.")
                continue
            if library.check_availability(title):  # verifica a disponibilidade do livro
                print(f"livro '{title}' está disponível.")
            else:
                print(f"livro '{title}' não está disponível.")
        
        elif choice == '5':  # opção para sair do programa
            print("saindo...")
            break  # encerra o loop e sai do programa
        
        else:
            print("opção inválida. tente novamente.")  # mensagem de erro para opção inválida

if __name__ == "__main__":
    main()  # chama a função main para iniciar o programa