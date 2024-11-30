# 6. Faça um programa para executar as operações abaixo em uma árvore binária.
# Menu
# 1 – Inserir número
# 2 – Mostrar se a arvore é estritamente binária
# 3 – Mostrar se a arvore é completa
# 4 – Mostrar se a arvore é cheia
# 5 – Sair

from binary_tree import BinaryTree

def main():
    tree = BinaryTree()

    while True:
        print("\nMenu:")
        print("1 - Inserir número")
        print("2 - Mostrar se a árvore é estritamente binária")
        print("3 - Mostrar se a árvore é completa")
        print("4 - Mostrar se a árvore é cheia")
        print("5 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            value = int(input("Digite um número para inserir: "))
            tree.insert(value)
        elif choice == "2":
            if tree.is_strictly_binary():
                print("A árvore é estritamente binária.")
            else:
                print("A árvore não é estritamente binária.")
        elif choice == "3":
            if tree.is_complete():
                print("A árvore é completa.")
            else:
                print("A árvore não é completa.")
        elif choice == "4":
            if tree.is_full():
                print("A árvore é cheia.")
            else:
                print("A árvore não é cheia.")
        elif choice == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
