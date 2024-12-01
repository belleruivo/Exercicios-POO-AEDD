from collection import *

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

