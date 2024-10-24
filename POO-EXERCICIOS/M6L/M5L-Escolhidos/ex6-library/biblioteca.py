from autor import Autor
from categoria import Categoria
from livro import Livro
from catalogo import Catalogo
from emprestimo import Emprestimo
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        # inicializa a classe biblioteca com um catálogo, listas de usuários, empréstimos, autores e categorias
        self.catalogo = Catalogo()
        self.usuarios = [] # lista vazia
        self.emprestimos = []
        self.autores = []
        self.categorias = []

    def cadastrar_livro(self, titulo, nome_autor, isbn, nome_categoria):
        # cadastra um novo livro na biblioteca
        try:
            # busca ou cria o autor e a categoria
            autor = self.buscar_ou_criar_autor(nome_autor)
            categoria = self.buscar_ou_criar_categoria(nome_categoria)
            # cria um novo livro e adiciona ao catálogo, autor e categoria
            livro = Livro(titulo, autor, isbn, categoria)
            self.catalogo.adicionar_livro(livro)
            autor.adicionar_livro(livro)
            categoria.adicionar_livro(livro)
            return f"Livro '{titulo}' cadastrado com sucesso."
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao cadastrar livro: {e}"

    def cadastrar_usuario(self, nome, user_id):
        # cadastra um novo usuário na biblioteca
        try:
            usuario = Usuario(nome, user_id)
            self.usuarios.append(usuario)
            return f"Usuário '{nome}' cadastrado com sucesso."
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao cadastrar usuário: {e}"

    def emprestar_livro(self, isbn, user_id):
        # realiza o empréstimo de um livro para um usuário
        livro = self.catalogo.buscar_livro(isbn)
        if livro and livro.disponivel:
            usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
            if usuario:
                emprestimo = Emprestimo(livro, usuario)
                self.emprestimos.append(emprestimo)
                usuario.adicionar_emprestimo(emprestimo)
                livro.alterar_disponibilidade(False)
                return f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'."
            else:
                return "Erro ao fazer empréstimo: Usuário não encontrado."
        else:
            return "Erro ao fazer empréstimo: Livro não disponível ou não encontrado."

    def devolver_livro(self, isbn, user_id):
        # realiza a devolução de um livro emprestado
        try:
            livro = self.catalogo.buscar_livro(isbn)
            if livro:
                usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
                if usuario:
                    emprestimo = next((e for e in self.emprestimos if e.livro.isbn == isbn and e.usuario.user_id == user_id and e.data_devolucao is None), None)
                    if emprestimo:
                        emprestimo.registrar_devolucao()
                        usuario.remover_emprestimo(emprestimo)
                        livro.alterar_disponibilidade(True)
                        return f"Livro '{livro.titulo}' devolvido com sucesso."
                    else:
                        return "Erro ao devolver livro: Empréstimo não encontrado."
                else:
                    return "Erro ao devolver livro: Usuário não encontrado."
            else:
                return "Erro ao devolver livro: Livro não encontrado."
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao devolver livro: {e}"

    def verificar_disponibilidade(self, isbn):
        # verifica a disponibilidade de um livro no catálogo
        try:
            livro = self.catalogo.buscar_livro(isbn)
            if livro:
                return livro.disponivel
            else:
                return "Erro ao verificar disponibilidade: Livro não encontrado."
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao verificar disponibilidade: {e}"

    def buscar_ou_criar_autor(self, nome):
        # busca um autor pelo nome ou cria um novo se não existir
        try:
            autor = next((a for a in self.autores if a.nome == nome), None)
            if not autor:
                autor = Autor(nome)
                self.autores.append(autor)
            return autor
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao buscar ou criar autor: {e}"

    def buscar_ou_criar_categoria(self, nome):
        # busca uma categoria pelo nome ou cria uma nova se não existir
        try:
            categoria = next((c for c in self.categorias if c.nome == nome), None)
            if not categoria:
                categoria = Categoria(nome)
                self.categorias.append(categoria)
            return categoria
        except ValueError as e:
            # retorna uma mensagem de erro caso ocorra uma exceção
            return f"Erro ao buscar ou criar categoria: {e}"

    def __repr__(self):
        # retorna uma representação string da biblioteca, incluindo o catálogo, usuários, empréstimos, autores e categorias
        return f"Biblioteca(catalogo={self.catalogo}, usuarios={self.usuarios}, emprestimos={self.emprestimos}, autores={self.autores}, categorias={self.categorias})"