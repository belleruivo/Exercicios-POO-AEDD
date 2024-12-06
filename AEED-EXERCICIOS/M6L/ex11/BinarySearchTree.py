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

    def successor(self, node, data):
        successor = None
        while node:
            if data < node.data:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.data if successor else None

    def predecessor(self, node, data):
        predecessor = None
        while node:
            if data > node.data:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.data if predecessor else None

    def minNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def maxNode(self, node):
        current = node
        while current.right:
            current = current.right
        return current
