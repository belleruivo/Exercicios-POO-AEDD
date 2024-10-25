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

# Injeção de Dependência:
# Semelhante ao Bibliotecario, a classe Relatorio recebe uma instância de Biblioteca para gerar relatórios. Isso permite que o Relatorio acesse as informações da biblioteca sem precisar conhecer os detalhes de implementação da mesma.