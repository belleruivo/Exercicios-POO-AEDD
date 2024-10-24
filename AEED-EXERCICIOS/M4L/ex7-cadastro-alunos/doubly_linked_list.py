from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_aprovados(self):
        current = self.head
        aprovados = []
        while current:
            if current.data.nota_final >= 7:
                aprovados.append(current.data.nome)
            current = current.next
        return aprovados