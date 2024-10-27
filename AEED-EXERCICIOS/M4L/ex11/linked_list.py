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

    def find_min_iterative(self):
        if self.head is None:
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def find_min_recursive(self, node=None):
        if node is None:
            node = self.head
        if node is None:
            return None
        if node.next is None:
            return node.data
        min_of_rest = self.find_min_recursive(node.next)
        return min(node.data, min_of_rest)

    def are_equal_iterative(self, other):
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

    def are_equal_recursive(self, node1=None, node2=None):
        if node1 is None and node2 is None:
            node1 = self.head
            node2 = other.head
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.data != node2.data:
            return False
        return self.are_equal_recursive(node1.next, node2.next)