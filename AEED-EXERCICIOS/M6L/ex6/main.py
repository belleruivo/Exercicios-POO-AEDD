# 6. Faça um programa para executar as operações abaixo em uma árvore binária.
# Menu
# 1 – Inserir número
# 2 – Mostrar se a arvore é estritamente binária
# 3 – Mostrar se a arvore é completa
# 4 – Mostrar se a arvore é cheia
# 5 – Sair

from binary_tree import BinaryTree

# Inserir número (livro):

# Quando você insere um livro (número) na estante (árvore), você precisa encontrar a posição correta para ele. Se a prateleira (nó) está vazia, você coloca o livro lá. Se não, você compara o número do livro com o número do livro já presente na prateleira e decide se deve colocá-lo na sub-prateleira da esquerda (se for menor) ou na sub-prateleira da direita (se for maior).
# Mostrar se a árvore é estritamente binária:

# Uma estante é estritamente binária se cada prateleira (nó) tem exatamente duas sub-prateleiras (filhos) ou nenhuma. Em outras palavras, cada prateleira deve estar completamente cheia ou completamente vazia.
# Mostrar se a árvore é completa:

# Uma estante é completa se todas as prateleiras estão preenchidas de maneira que não haja lacunas. Isso significa que todas as prateleiras são preenchidas da esquerda para a direita, sem deixar espaços vazios.
# Mostrar se a árvore é cheia:

# Uma estante é cheia se todas as prateleiras têm exatamente duas sub-prateleiras ou nenhuma. Isso é semelhante à estante estritamente binária, mas com a condição adicional de que todas as prateleiras devem estar completamente preenchidas.

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
