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
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def find_level(self, value):
        return self._find_level_recursive(self.root, value, 0)

    def _find_level_recursive(self, node, value, level):
        if node is None:
            return -1  # Retorna -1 se o valor não for encontrado
        if node.value == value:
            return level
        if value < node.value:
            return self._find_level_recursive(node.left, value, level + 1)
        return self._find_level_recursive(node.right, value, level + 1)

# Menu principal
def main():
    tree = BinaryTree()

    while True:
        print("\nMenu")
        print("1 – Inserir número")
        print("2 – Mostrar a altura da árvore")
        print("3 – Mostrar o nível de um nó")
        print("4 – Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            try:
                num = int(input("Digite o número a ser inserido: "))
                tree.insert(num)
                print(f"Número {num} inserido com sucesso!")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif choice == "2":
            print(f"A altura da árvore é: {tree.height()}")
        elif choice == "3":
            try:
                num = int(input("Digite o número para encontrar o nível: "))
                level = tree.find_level(num)
                if level == -1:
                    print("Número não encontrado na árvore.")
                else:
                    print(f"O nível do número {num} é: {level}")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif choice == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
