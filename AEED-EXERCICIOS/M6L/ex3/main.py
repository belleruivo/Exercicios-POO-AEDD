'''
Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar todos
3 – Mostrar a sub-árvore direita de um nó
4 – Mostrar a sub-árvore esquerda de um nó
5 – Sair
'''

from BinarySearchTree import BinarySearchTree

def menu():
    print("Menu")
    print("1 – Inserir número")
    print("2 – Mostrar todos")
    print("3 – Mostrar a sub-árvore direita de um nó")
    print("4 – Mostrar a sub-árvore esquerda de um nó")
    print("5 – Sair")

if __name__ == "__main__":
    bst = BinarySearchTree()
    while True:
        menu()
        choice = int(input("Escolha uma opção: "))
        if choice == 1:
            data = int(input("Digite um número para inserir: "))
            bst.insert(bst.root, data)
        elif choice == 2:
            bst.printInOrder(bst.root)
            print()
        elif choice == 3:
            data = int(input("Digite o valor do nó para ver a sub-árvore direita: "))
            bst.showRightSubTree(data)
        elif choice == 4:
            data = int(input("Digite o valor do nó para ver a sub-árvore esquerda: "))
            bst.showLeftSubTree(data)
        elif choice == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
