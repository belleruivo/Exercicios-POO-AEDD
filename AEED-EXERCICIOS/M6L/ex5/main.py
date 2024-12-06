'''5. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar a altura da arvore
3 – Mostrar o nível de um nó
4 – Sair'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_node(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_node(current.right, new_node)

    def get_height(self, node=None):
        if node is None:
            if node is self.root:
                return 0
            return 0
        left_height = self.get_height(node.left) if node.left else 0
        right_height = self.get_height(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

    def get_level(self, value, node=None, level=0):
        if node is None:
            node = self.root
        if node is None:
            return -1  # Árvore vazia ou nó não encontrado
        if node.value == value:
            return level
        elif value < node.value:
            return self.get_level(value, node.left, level + 1)
        else:
            return self.get_level(value, node.right, level + 1)

def menu():
    tree = BinaryTree()
    while True:
        print("\nMenu:")
        print("1 – Inserir número")
        print("2 – Mostrar a altura da árvore")
        print("3 – Mostrar o nível de um nó")
        print("4 – Sair")
        try:
            option = int(input("Escolha uma opção: "))
            if option == 1:
                value = int(input("Digite o número a ser inserido: "))
                tree.insert(value)
                print(f"Número {value} inserido na árvore.")
            elif option == 2:
                height = tree.get_height(tree.root)  # Passar explicitamente a raiz
                print(f"A altura da árvore é: {height}")
            elif option == 3:
                value = int(input("Digite o valor do nó para encontrar o nível: "))
                level = tree.get_level(value)
                if level == -1:
                    print(f"Nó {value} não encontrado.")
                else:
                    print(f"O nível do nó {value} é: {level}")
            elif option == 4:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    menu()
