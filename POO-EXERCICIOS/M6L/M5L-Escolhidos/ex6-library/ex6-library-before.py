'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, aplicando a
associação de classes.

Uma boa maneira de criar esse exercício é seguindo o seguinte roteiro:

- descreva em no máximo 200 palavras o que é um objeto específico e o que ele faz. 
- Liste os substantivos e verbos separadamente. Cada substantivo corresponde a um objeto que precisará ser
construído para implementar um sistema. 
- Selecione 5 dos objetos que você listou e, para cada um, liste vários atributos e comportamentos. 
- Perceba também as associações e implemente-as.
- Descreva brevemente como esses objetos interagem entre si e com outros objetos na sua descrição. 

Estes passos que você seguiu são típicos do projeto orientado a objetos.
'''

from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, categoria):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.categoria = categoria

    def change_availability(self, status):
        self.available = status

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, available={self.available}, categoria={self.categoria})"

class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def __repr__(self):
        return f"Autor(nome={self.nome}, livros={[livro.title for livro in self.livros]})"

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def __repr__(self):
        return f"Categoria(nome={self.nome}, livros={[livro.title for livro in self.livros]})"

class Usuario:
    def __init__(self, nome, user_id):
        self.nome = nome
        self.user_id = user_id
        self.livros_emprestados = []

    def adicionar_emprestimo(self, emprestimo):
        self.livros_emprestados.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self.livros_emprestados.remove(emprestimo)

    def __repr__(self):
        return f"Usuario(nome={self.nome}, user_id={self.user_id}, livros_emprestados={self.livros_emprestados})"

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def registrar_devolucao(self):
        self.data_devolucao = datetime.now()

    def __repr__(self):
        return f"Emprestimo(livro={self.livro.title}, usuario={self.usuario.nome}, data_emprestimo={self.data_emprestimo}, data_devolucao={self.data_devolucao})"

class Catalogo:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def __repr__(self):
        return f"Catalogo(livros={self.livros})"

class Biblioteca:
    def __init__(self):
        self.catalogo = Catalogo()
        self.usuarios = []
        self.emprestimos = []
        self.autores = []
        self.categorias = []

    def cadastrar_livro(self, titulo, autor_nome, isbn, categoria_nome):
        autor = self.buscar_ou_criar_autor(autor_nome)
        categoria = self.buscar_ou_criar_categoria(categoria_nome)
        livro = Book(titulo, autor, isbn, categoria)
        self.catalogo.adicionar_livro(livro)
        autor.adicionar_livro(livro)
        categoria.adicionar_livro(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, nome, user_id):
        usuario = Usuario(nome, user_id)
        self.usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def emprestar_livro(self, isbn, user_id):
        livro = self.catalogo.buscar_livro(isbn)
        if livro and livro.available:
            usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
            if usuario:
                emprestimo = Emprestimo(livro, usuario)
                self.emprestimos.append(emprestimo)
                usuario.adicionar_emprestimo(emprestimo)
                livro.change_availability(False)
                print(f"Livro '{livro.title}' emprestado para '{usuario.nome}'.")
            else:
                print("Usuário não encontrado.")
        else:
            print("Livro não disponível ou não encontrado.")

    def devolver_livro(self, isbn, user_id):
        livro = self.catalogo.buscar_livro(isbn)
        if livro:
            usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
            if usuario:
                emprestimo = next((e for e in self.emprestimos if e.livro.isbn == isbn and e.usuario.user_id == user_id and e.data_devolucao is None), None)
                if emprestimo:
                    emprestimo.registrar_devolucao()
                    usuario.remover_emprestimo(emprestimo)
                    livro.change_availability(True)
                    print(f"Livro '{livro.title}' devolvido por '{usuario.nome}'.")
                else:
                    print("Empréstimo não encontrado.")
            else:
                print("Usuário não encontrado.")
        else:
            print("Livro não encontrado.")

    def verificar_disponibilidade(self, isbn):
        livro = self.catalogo.buscar_livro(isbn)
        if livro:
            return livro.available
        return False

    def buscar_ou_criar_autor(self, nome):
        autor = next((a for a in self.autores if a.nome == nome), None)
        if not autor:
            autor = Autor(nome)
            self.autores.append(autor)
        return autor

    def buscar_ou_criar_categoria(self, nome):
        categoria = next((c for c in self.categorias if c.nome == nome), None)
        if not categoria:
            categoria = Categoria(nome)
            self.categorias.append(categoria)
        return categoria

    def __repr__(self):
        return f"Biblioteca(catalogo={self.catalogo}, usuarios={self.usuarios}, emprestimos={self.emprestimos}, autores={self.autores}, categorias={self.categorias})"

def cadastrar_livro(biblioteca):
    titulo = input("Digite o título do livro: ").strip()
    if not titulo:
        print("O título do livro não pode ser vazio.")
        return
    autor = input("Digite o autor do livro: ").strip()
    if not autor:
        print("O autor do livro não pode ser vazio.")
        return
    isbn = input("Digite o ISBN do livro: ").strip()
    if not isbn:
        print("O ISBN do livro não pode ser vazio.")
        return
    categoria = input("Digite a categoria do livro: ").strip()
    if not categoria:
        print("A categoria do livro não pode ser vazia.")
        return
    biblioteca.cadastrar_livro(titulo, autor, isbn, categoria)

def cadastrar_usuario(biblioteca):
    nome = input("Digite o nome do usuário: ").strip()
    if not nome:
        print("O nome do usuário não pode ser vazio.")
        return
    try:
        user_id = int(input("Digite o ID do usuário: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return
    biblioteca.cadastrar_usuario(nome, user_id)

def fazer_emprestimo(biblioteca):
    isbn = input("Digite o ISBN do livro: ").strip()
    if not isbn:
        print("O ISBN do livro não pode ser vazio.")
        return
    try:
        user_id = int(input("Digite o ID do usuário: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return
    biblioteca.emprestar_livro(isbn, user_id)

def devolver_livro(biblioteca):
    isbn = input("Digite o ISBN do livro: ").strip()
    if not isbn:
        print("O ISBN do livro não pode ser vazio.")
        return
    try:
        user_id = int(input("Digite o ID do usuário: "))
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return
    biblioteca.devolver_livro(isbn, user_id)

def verificar_disponibilidade(biblioteca):
    isbn = input("Digite o ISBN do livro: ").strip()
    if not isbn:
        print("O ISBN do livro não pode ser vazio.")
        return
    if biblioteca.verificar_disponibilidade(isbn):
        print(f"Livro '{isbn}' está disponível.")
    else:
        print(f"Livro '{isbn}' não está disponível.")

def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Fazer empréstimo")
        print("4. Devolver livro")
        print("5. Verificar disponibilidade")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_livro(biblioteca)
        elif escolha == '2':
            cadastrar_usuario(biblioteca)
        elif escolha == '3':
            fazer_emprestimo(biblioteca)
        elif escolha == '4':
            devolver_livro(biblioteca)
        elif escolha == '5':
            verificar_disponibilidade(biblioteca)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()