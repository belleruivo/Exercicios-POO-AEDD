from node import Node

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def push(self, new_data):
        new_node = Node(new_data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Empty stack")
            return None
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    def peek(self):
        return None if self.is_empty() else self.head.data