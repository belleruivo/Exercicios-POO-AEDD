from nodeTree import NodeTree

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, node, data):
        if self.root is None:
            self.root = NodeTree(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            elif data > node.data:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)

    def search(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def printInOrder(self, node):
        if node:
            self.printInOrder(node.left)
            print(f'{node.data}', end=" ")
            self.printInOrder(node.right)

    def printSubTree(self, node):
        if node:
            self.printInOrder(node)
            print()

    def showRightSubTree(self, data):
        node = self.search(self.root, data)
        if node and node.right:
            self.printSubTree(node.right)
        else:
            print("Nó não encontrado ou não possui sub-árvore direita.")

    def showLeftSubTree(self, data):
        node = self.search(self.root, data)
        if node and node.left:
            self.printSubTree(node.left)
        else:
            print("Nó não encontrado ou não possui sub-árvore esquerda.")
