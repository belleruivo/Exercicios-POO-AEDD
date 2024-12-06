from nodeTree import NodeTree
import random

class BinaryTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, node, data):
        if self.root is None:
            self.root = NodeTree(data)
        else:
            if random.choice([True, False]):
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            else:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)

    def printInOrder(self, node):
        if node:
            self.printInOrder(node.left)
            print(f'{node.data}', end=" ")
            self.printInOrder(node.right)

    def printPreOrder(self, node):
        if node:
            print(f'{node.data}', end=" ")
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if node:
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(f'{node.data}', end=" ")

    def maxNode(self, node):
        if node is None:
            return float('-inf')
        max_left = self.maxNode(node.left)
        max_right = self.maxNode(node.right)
        return max(node.data, max_left, max_right)

    def imprimeRelacoes(self):
        def percorreEImprime(no):
            if no is None:
                return

            if no.left:
                print(f"O nó de valor {no.left.data} é filho esquerdo de {no.data}")
            else:
                print(f"O nó de valor {no.data} não tem filho esquerdo")

            if no.right:
                print(f"O nó de valor {no.right.data} é filho direito de {no.data}")
            else:
                print(f"O nó de valor {no.data} não tem filho direito")

            percorreEImprime(no.left)
            percorreEImprime(no.right)

        if self.root is None:
            print("A árvore está vazia.")
        else:
            percorreEImprime(self.root)
