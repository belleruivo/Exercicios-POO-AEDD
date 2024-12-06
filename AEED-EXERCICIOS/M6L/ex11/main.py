'''
Adicione os métodos sucessor e antecessor a uma Árvore Binária de Busca. Cada método espera um item como argumento e retorna um item ou None. Um sucessor é o menor item na árvore que é maior do que o determinado item. Um predecessor é o maior item na árvore que é menor do que o determinado item. Observe que o
sucessor pode existir mesmo se o item fornecido não estiver presente na árvore.
'''

from BinarySearchTree import BinarySearchTree

def menu():
    print("\nMenu")
    print("1 – Inserir número")
    print("2 – Mostrar todos")
    print("3 – Encontrar sucessor")
    print("4 – Encontrar antecessor")
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
            data = int(input("Digite o valor do nó para encontrar o sucessor: "))
            print(f'Sucessor de {data} é {bst.successor(bst.root, data)}')
        elif choice == 4:
            data = int(input("Digite o valor do nó para encontrar o antecessor: "))
            print(f'Antecessor de {data} é {bst.predecessor(bst.root, data)}')
        elif choice == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")
