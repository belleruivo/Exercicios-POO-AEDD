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

    @classmethod
    def adicionar_livro(cls, biblioteca, titulo, quantidade=1):  # método para adicionar livros
        if titulo in biblioteca.livros:  # se o livro já estiver no dicionário
            biblioteca.livros[titulo] += quantidade  # incrementa a quantidade existente
        else:
            biblioteca.livros[titulo] = quantidade  # adiciona o livro com a quantidade especificada

    def emprestar_livro(self, titulo):  # método para emprestar um livro
        if titulo in self.livros and self.livros[titulo] > 0:  # verifica se o livro está disponível
            self.livros[titulo] -= 1  # decrementa a quantidade do livro
            return True  # retorna true se o empréstimo for bem-sucedido
        return False  # retorna false se o livro não estiver disponível

    def devolver_livro(self, titulo):  # método para devolver um livro
        if titulo in self.livros:  # verifica se o livro está cadastrado
            self.livros[titulo] += 1  # incrementa a quantidade do livro
        else:
            print(f"livro '{titulo}' não está cadastrado na biblioteca.")  # mensagem de erro se o livro não estiver cadastrado

    @staticmethod
    def verificar_disponibilidade(biblioteca, titulo):  # método para verificar a disponibilidade de um livro
        return biblioteca.livros.get(titulo, 0) > 0  # retorna true se o livro estiver disponível, caso contrário, false

def cadastrar_livro(biblioteca):
    titulo = input("digite o título do livro: ").strip()  # solicita o título do livro
    if not titulo:  # verifica se o título não está vazio
        print("o título do livro não pode ser vazio.")
        return
    try:
        quantidade = int(input("digite a quantidade: "))  # solicita a quantidade do livro
        if quantidade <= 0:  # verifica se a quantidade é um número inteiro positivo
            raise ValueError
    except ValueError:
        print("quantidade inválida. deve ser um número inteiro positivo.")
        return
    Library.adicionar_livro(biblioteca, titulo, quantidade)  # adiciona o livro à biblioteca
    print(f"livro '{titulo}' cadastrado com sucesso!")

def fazer_emprestimo(biblioteca):
    titulo = input("digite o título do livro: ").strip()  # solicita o título do livro
    if not titulo:  # verifica se o título não está vazio
        print("o título do livro não pode ser vazio.")
        return
    if biblioteca.emprestar_livro(titulo):  # tenta emprestar o livro
        print(f"empréstimo do livro '{titulo}' realizado com sucesso!")
    else:
        print(f"livro '{titulo}' não disponível para empréstimo.")

def devolver_livro(biblioteca):
    titulo = input("digite o título do livro: ").strip()  # solicita o título do livro
    if not titulo:  # verifica se o título não está vazio
        print("o título do livro não pode ser vazio.")
        return
    if titulo in biblioteca.livros:  # verifica se o livro está cadastrado
        biblioteca.devolver_livro(titulo)  # devolve o livro
        print(f"livro '{titulo}' devolvido com sucesso!")
    else:
        print(f"livro '{titulo}' não está cadastrado na biblioteca.")

def verificar_disponibilidade(biblioteca):
    titulo = input("digite o título do livro: ").strip()  # solicita o título do livro
    if not titulo:  # verifica se o título não está vazio
        print("o título do livro não pode ser vazio.")
        return
    if Library.verificar_disponibilidade(biblioteca, titulo):  # verifica a disponibilidade do livro
        print(f"livro '{titulo}' está disponível.")
    else:
        print(f"livro '{titulo}' não está disponível.")

def main():
    biblioteca = Library()  # cria uma instância da classe library
    
    while True:
        print("\n1. cadastrar livro")
        print("2. fazer empréstimo")
        print("3. devolver livro")
        print("4. verificar disponibilidade")
        print("5. sair")
        
        escolha = input("escolha uma opção: ")  # solicita ao usuário que escolha uma opção
        
        if escolha == '1':  # opção para cadastrar um livro
            cadastrar_livro(biblioteca)
        elif escolha == '2':  # opção para fazer empréstimo de um livro
            fazer_emprestimo(biblioteca)
        elif escolha == '3':  # opção para devolver um livro
            devolver_livro(biblioteca)
        elif escolha == '4':  # opção para verificar a disponibilidade de um livro
            verificar_disponibilidade(biblioteca)
        elif escolha == '5':  # opção para sair do programa
            print("saindo...")
            break  # encerra o loop e sai do programa
        else:
            print("opção inválida. tente novamente.")  # mensagem de erro para opção inválida

if __name__ == "__main__":
    main()  # chama a função main para iniciar o programa