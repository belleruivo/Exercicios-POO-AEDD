from collection import Livro, Revista, DVD, CD

def exibir_menu():
    print("\nSelecione o tipo de acervo:")
    print("1. Livro")
    print("2. Revista")
    print("3. DVD")
    print("4. CD")

def obter_dados_comuns():
    titulo = input("Título: ").strip()
    while True:
        try:
            ano = int(input("Ano: ").strip())
            break
        except ValueError:
            print("Entrada inválida! O ano deve ser um número. Tente novamente.\n")
    return titulo, ano

def criar_acervo():
    while True:
        exibir_menu()
        tipo = input("Digite o número correspondente: ").strip()

        if tipo not in {"1", "2", "3", "4"}:
            print("Opção inválida! Por favor, tente novamente.\n")
            continue

        titulo, ano = obter_dados_comuns()

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
        item = criar_acervo()
        if item:
            acervo.append(item)
            print(f"Item '{item.titulo}' adicionado com sucesso!\n")
        
        while True:
            continuar = input("Deseja adicionar outro item? (s/n): ").strip().lower()
            if continuar in {"s", "n"}:
                break
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.\n")
        
        if continuar == "n":
            break
    
    if acervo:
        print("\nAcervo da Biblioteca:")
        for item in acervo:
            print(item.descricao())
    else:
        print("Nenhum item foi adicionado ao acervo.")

if __name__ == "__main__":
    main()

