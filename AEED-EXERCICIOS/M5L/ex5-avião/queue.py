from node import Node

class Queue:
    def __init__(self):
        self.head = None  # Primeiro avião da fila
        self.tail = None  # Último avião da fila
        self.size = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, airplane):
        new_node = Node(airplane)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Não há aviões na fila.")
            return None
        removed_airplane = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return removed_airplane

    def peek(self):
        return self.head.data if self.head else None

    def list_airplanes(self):
        current = self.head
        airplanes = []
        while current:
            airplanes.append(current.data)
            current = current.next
        return airplanes