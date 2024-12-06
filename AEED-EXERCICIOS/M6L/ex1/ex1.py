'''1. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar todos os números
3 – Mostrar o maior número
4 – Mostrar o menor número
5 – Mostrar quantos números têm na árvore
6 – Sair'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert_recursive(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif value > current_node.value:
            if current_node.right:
                self._insert_recursive(current_node.right, value)
            else:
                current_node.right = Node(value)

    def show_all(self):
        values = []
        self._in_order_traversal(self.root, values)
        return values

    def _in_order_traversal(self, node, values):
        if node:
            self._in_order_traversal(node.left, values)
            values.append(node.value)
            self._in_order_traversal(node.right, values)

    def find_max(self):
        current = self.root
        if not current:
            return None
        while current.right:
            current = current.right
        return current.value

    def find_min(self):
        current = self.root
        if not current:
            return None
        while current.left:
            current = current.left
        return current.value

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

def main():
    tree = BinaryTree()
    while True:
        print("\nMenu")
        print("1 – Inserir número")
        print("2 – Mostrar todos os números")
        print("3 – Mostrar o maior número")
        print("4 – Mostrar o menor número")
        print("5 – Mostrar quantos números têm na árvore")
        print("6 – Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            number = int(input("Digite um número para inserir: "))
            tree.insert(number)
        elif choice == "2":
            numbers = tree.show_all()
            print("Números na árvore:", numbers)
        elif choice == "3":
            max_value = tree.find_max()
            if max_value is not None:
                print("Maior número:", max_value)
            else:
                print("A árvore está vazia.")
        elif choice == "4":
            min_value = tree.find_min()
            if min_value is not None:
                print("Menor número:", min_value)
            else:
                print("A árvore está vazia.")
        elif choice == "5":
            count = tree.count_nodes()
            print("Quantidade de números na árvore:", count)
        elif choice == "6":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
