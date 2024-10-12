'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a associação bilateral.

'''

class Library:
    def __init__(self, name):  # inicializa a classe Library
        self.name = name  # nome da biblioteca
        self.books = {}  # dicionário para armazenar livros e suas quantidades
        self.users = {}  # dicionário para armazenar os usuários e seus empréstimos

    def adicionar_livro(self, titulo, quantidade=1):  # método para adicionar livros
        if titulo in self.books:
            self.books[titulo] += quantidade  # incrementa a quantidade de livros
        else:
            self.books[titulo] = quantidade  # adiciona novo livro
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def emprestar_livro(self, titulo, user):  # método para emprestar um livro a um usuário
        if titulo in self.books and self.books[titulo] > 0:  # verifica se o livro está disponível
            self.books[titulo] -= 1  # diminui a quantidade disponível do livro
            user.adicionar_emprestimo(self, titulo)  # associa o livro ao usuário
            print(f"Empréstimo do livro '{titulo}' realizado para {user.name}.")
            return True
        print(f"Livro '{titulo}' não está disponível para empréstimo.")
        return False

    def devolver_livro(self, titulo, user):  # método para devolver um livro
        if titulo in user.livros_emprestados.get(self.name, []):  # verifica se o livro está com o usuário
            self.books[titulo] += 1  # incrementa a quantidade disponível na biblioteca
            user.remover_emprestimo(self, titulo)  # remove o livro dos empréstimos do usuário
            print(f"Livro '{titulo}' devolvido por {user.name}.")
        else:
            print(f"{user.name} não tem o livro '{titulo}' emprestado desta biblioteca.")

    def verificar_disponibilidade(self, titulo):  # método para verificar disponibilidade
        if self.books.get(titulo, 0) > 0:
            return True
        return False

    def registrar_usuario(self, user):  # método para registrar usuário na biblioteca
        if user.name not in self.users:
            self.users[user.name] = user
            print(f"Usuário {user.name} registrado na biblioteca {self.name}.")
        else:
            print(f"Usuário {user.name} já está registrado nesta biblioteca.")

class User:
    def __init__(self, name):  # inicializa a classe User
        self.name = name  # nome do usuário
        self.livros_emprestados = {}  # dicionário com os livros emprestados em cada biblioteca

    def adicionar_emprestimo(self, biblioteca, titulo):  # associa o empréstimo do livro
        if biblioteca.name not in self.livros_emprestados:
            self.livros_emprestados[biblioteca.name] = []
        self.livros_emprestados[biblioteca.name].append(titulo)  # adiciona o livro na lista de empréstimos

    def remover_emprestimo(self, biblioteca, titulo):  # remove o empréstimo do livro
        if biblioteca.name in self.livros_emprestados:
            if titulo in self.livros_emprestados[biblioteca.name]:
                self.livros_emprestados[biblioteca.name].remove(titulo)  # remove o livro devolvido

    def verificar_emprestimos(self):  # exibe os livros que o usuário tem emprestados
        print(f"Empréstimos de {self.name}:")
        for biblioteca, livros in self.livros_emprestados.items():
            if livros:
                print(f"Biblioteca {biblioteca}: {', '.join(livros)}")
            else:
                print(f"Biblioteca {biblioteca}: sem livros emprestados.")


# Função principal para rodar o sistema
def main():
    # Criando uma biblioteca
    biblioteca1 = Library("Biblioteca Central")
    
    # Criando usuários
    usuario1 = User("Isabelle")
    usuario2 = User("Arthur")
    
    # Registrando usuários na biblioteca
    biblioteca1.registrar_usuario(usuario1)
    biblioteca1.registrar_usuario(usuario2)
    
    # Adicionando livros à biblioteca
    biblioteca1.adicionar_livro("O Senhor dos Anéis", 2)
    biblioteca1.adicionar_livro("1984", 3)
    
    # Usuário 1 faz um empréstimo
    biblioteca1.emprestar_livro("O Senhor dos Anéis", usuario1)
    
    # Verificar empréstimos do usuário 1
    usuario1.verificar_emprestimos()
    
    # Usuário 1 devolve o livro
    biblioteca1.devolver_livro("O Senhor dos Anéis", usuario1)
    
    # Verificar empréstimos novamente
    usuario1.verificar_emprestimos()

    # Usuário 2 tenta emprestar um livro indisponível
    biblioteca1.emprestar_livro("1984", usuario2)
    
    # Verificar disponibilidade de um livro
    if biblioteca1.verificar_disponibilidade("O Senhor dos Anéis"):
        print("O livro 'O Senhor dos Anéis' está disponível.")
    else:
        print("O livro 'O Senhor dos Anéis' não está disponível.")

if __name__ == "__main__":
    main()
