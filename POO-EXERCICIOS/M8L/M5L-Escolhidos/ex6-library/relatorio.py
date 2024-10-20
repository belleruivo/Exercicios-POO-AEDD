class Relatorio:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_emprestimos(self):
        print("\nRelatório de Empréstimos:")
        for usuario in self.biblioteca.usuarios.values():
            print(f"Usuário: {usuario.nome}")
            if usuario.emprestimos:
                print(f"  Livros Emprestados: {', '.join(usuario.emprestimos)}")
            else:
                print("  Nenhum livro emprestado.")
