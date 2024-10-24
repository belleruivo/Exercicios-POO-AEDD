from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def copy_from_array_iterative(self, array):
        for item in array:
            self.insert(item)

    def copy_from_array_recursive(self, array, index=0):
        if index < len(array):
            self.insert(array[index])
            self.copy_from_array_recursive(array, index + 1)

    def copy_to_array_iterative(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    def copy_to_array_recursive(self, node=None, array=None):
        if array is None:
            array = []
        if node is None:
            node = self.head
        if node is not None:
            array.append(node.data)
            self.copy_to_array_recursive(node.next, array)
        return array