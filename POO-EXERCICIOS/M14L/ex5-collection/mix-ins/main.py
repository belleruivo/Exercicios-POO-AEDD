from collection import *
# Main function
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

        titulo = input("\nTítulo: ").strip()
        while True:
            try:
                ano = int(input("Ano: ").strip())
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

def main():
    acervo = []
    while True:
        print("\nSelecione uma ação:")
        print("1. Adicionar Item")
        print("2. Emprestar Item")
        escolha = input("Digite o número correspondente: ").strip()

        if escolha == "1":
            item = criar_acervo()
            if item:
                acervo.append(item)
                print("Item adicionado com sucesso!\n")

        elif escolha == "2":
            if not acervo:
                print("O acervo está vazio! Adicione um item primeiro.\n")
                continue
            
            print("\nItens do acervo disponíveis para empréstimo:")
            for idx, item in enumerate(acervo, 1):
                print(f"{idx}. {item.descricao()}")
            
            while True:
                try:
                    escolha_item = int(input("\nEscolha o número do item que deseja emprestar: ").strip())
                    if 1 <= escolha_item <= len(acervo):
                        item = acervo[escolha_item - 1]
                        if isinstance(item, Borrowable):  # Verifica se o item pode ser emprestado
                            print(item.emprestar())
                        else:
                            print(f"'{item.titulo}' não pode ser emprestado!")
                        break
                    else:
                        print("Número inválido. Tente novamente.\n")
                except ValueError:
                    print("Entrada inválida! Digite um número.\n")
        else:
            print("Opção inválida! Tente novamente.")

        while True:
            continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
            if continuar in {"s", "n"}:
                break
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.\n")
        
        if continuar == "n":
            break

main()
