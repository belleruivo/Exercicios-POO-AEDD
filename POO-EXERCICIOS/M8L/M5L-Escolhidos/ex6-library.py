'''
Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência..

'''

class Livro:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def emprestar(self):
        if self.quantidade > 0:
            self.quantidade -= 1
            return True
        return False

    def devolver(self):
        self.quantidade += 1

    def disponivel(self):
        return self.quantidade > 0


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.emprestimos = []

    def realizar_emprestimo(self, livro):
        if livro.emprestar():
            self.emprestimos.append(livro.titulo)
            print(f"Empréstimo do livro '{livro.titulo}' realizado para {self.nome}!")
            return True
        print(f"Livro '{livro.titulo}' não disponível para empréstimo.")
        return False

    def devolver_livro(self, livro):
        if livro.titulo in self.emprestimos:
            livro.devolver()
            self.emprestimos.remove(livro.titulo)
            print(f"{self.nome} devolveu o livro '{livro.titulo}' com sucesso!")
            return True
        print(f"{self.nome} não tem o livro '{livro.titulo}' para devolver.")
        return False


class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

    def efetuar_emprestimo(self):
        return self.usuario.realizar_emprestimo(self.livro)

    def efetuar_devolucao(self):
        return self.usuario.devolver_livro(self.livro)


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}

    def adicionar_livro(self, titulo, quantidade=1):
        if titulo in self.livros:
            self.livros[titulo].quantidade += quantidade
        else:
            self.livros[titulo] = Livro(titulo, quantidade)
        print(f"Livro '{titulo}' adicionado/atualizado com sucesso!")

    def cadastrar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = Usuario(nome)
            print(f"Usuário '{nome}' cadastrado com sucesso!")
        else:
            print(f"Usuário '{nome}' já está cadastrado.")

    def emprestar_livro(self, nome_usuario, titulo_livro):
        usuario = self.usuarios.get(nome_usuario)
        livro = self.livros.get(titulo_livro)

        if usuario and livro:
            emprestimo = Emprestimo(usuario, livro)
            emprestimo.efetuar_emprestimo()
        else:
            print("Usuário ou livro não encontrados.")

    def devolver_livro(self, nome_usuario, titulo_livro):
        usuario = self.usuarios.get(nome_usuario)
        livro = self.livros.get(titulo_livro)

        if usuario and livro:
            emprestimo = Emprestimo(usuario, livro)
            emprestimo.efetuar_devolucao()
        else:
            print("Usuário ou livro não encontrados.")


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Fazer empréstimo")
        print("4. Devolver livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            titulo = input("Título do livro: ").strip()
            try:
                quantidade = int(input("Quantidade: ").strip())
                biblioteca.adicionar_livro(titulo, quantidade)
            except ValueError:
                print("Quantidade inválida. Deve ser um número inteiro.")

        elif opcao == '2':
            nome = input("Nome do usuário: ").strip()
            biblioteca.cadastrar_usuario(nome)

        elif opcao == '3':
            nome_usuario = input("Nome do usuário: ").strip()
            titulo_livro = input("Título do livro: ").strip()
            biblioteca.emprestar_livro(nome_usuario, titulo_livro)

        elif opcao == '4':
            nome_usuario = input("Nome do usuário: ").strip()
            titulo_livro = input("Título do livro: ").strip()
            biblioteca.devolver_livro(nome_usuario, titulo_livro)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
