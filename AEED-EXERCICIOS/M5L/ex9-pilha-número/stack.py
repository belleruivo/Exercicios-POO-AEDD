from node import Node

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("A pilha está vazia. Não há números para excluir.")
            return None
        else:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def get_all_elements(self):
        elements = []
        current = self.head
        while current:
            elements.insert(0, current.data) 
            current = current.next
        return elements

    def remove(self, value):
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return value
            prev = current
            current = current.next
        return None