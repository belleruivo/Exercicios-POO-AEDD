from node import Node

class LinkedList:
    def __init__(self):
        self.head = None  # cabeça da lista

    def append(self, data):
        """ Adiciona um novo nó ao final da lista. """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __iter__(self):
        """ Permite a iteração sobre a lista encadeada. """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def is_digit(self, char):
        """ Retorna True se o caractere é um dígito, False caso contrário. """
        return char.isdigit()
