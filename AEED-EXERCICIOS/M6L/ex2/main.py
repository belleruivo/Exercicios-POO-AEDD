from binary_tree import BinaryTree

def main():
    # cria a árvore binária
    tree = BinaryTree()
    
    while True:
        # exibe o menu
        print("\nMenu")
        print("1 – Inserir número")
        print("2 – Mostrar nós folha")
        print("3 – Mostrar os nós ancestrais de um nó")
        print("4 – Mostrar os descendentes de um nó")
        print("5 – Mostrar o nó pai e os nós filhos de um nó")
        print("6 – Sair")

        try:
            option = int(input("Escolha uma opção: "))
            
            if option == 1:
                # insere múltiplos números
                nums = input("Digite os números separados por espaços: ")
                for num in nums.split():
                    try:
                        tree.insert(int(num))  # tenta converter e inserir
                    except ValueError:
                        print(f"'{num}' não é um número válido e será ignorado.")
                print("Números inseridos com sucesso!")
            
            elif option == 2:
                # exibe os nós folha
                leaf_nodes = tree.get_leaf_nodes()
                print("Nós folha:", leaf_nodes)
            
            elif option == 3:
                # exibe os ancestrais de um nó
                node = int(input("Digite o nó: "))
                ancestors = tree.find_ancestors(node)
                print(f"Ancestrais de {node}:", ancestors)
            
            elif option == 4:
                # exibe os descendentes de um nó
                node = int(input("Digite o nó: "))
                descendants = tree.find_descendants(node)
                print(f"Descendentes de {node}:", descendants)
            
            elif option == 5:
                # exibe o pai e os filhos de um nó
                try:
                    node = int(input("Digite o nó: "))
                    result = tree.find_parent_and_children(node)
                    parent = result["pai"]
                    left_child = result["filho_esquerda"]
                    right_child = result["filho_direita"]

                    print(f"Pai de {node}: {parent}")
                    print(f"Filho à esquerda: {left_child}")
                    print(f"Filho à direita: {right_child}")
                except ValueError as e:
                    print(e)  # Exibe a mensagem de erro se o nó não for encontrado
            
            elif option == 6:
                print("Saindo do programa...")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Entrada inválida. Digite um número para selecionar uma opção.")

if __name__ == "__main__":
    main()
