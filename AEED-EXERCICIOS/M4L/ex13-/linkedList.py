from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after_k(self, k, data):
        if k < 0:
            print("Índice inválido!")
            return
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count < k:
            current = current.next
            count += 1
        if current is None:
            print("Índice fora do alcance da lista!")
            return
        new_node.next = current.next
        current.next = new_node

    def swap_iterative(self, x, y):
        if x == y:
            return

        prev_x = None
        curr_x = self.head
        while curr_x and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next

        prev_y = None
        curr_y = self.head
        while curr_y and curr_y.data != y:
            prev_y = curr_y
            curr_y = curr_y.next

        if not curr_x or not curr_y:
            print("Um ou ambos os elementos não estão na lista.")
            return

        if prev_x:
            prev_x.next = curr_y
        else:
            self.head = curr_y

        if prev_y:
            prev_y.next = curr_x
        else:
            self.head = curr_x

        curr_x.next, curr_y.next = curr_y.next, curr_x.next

    def swap_recursive(self, x, y):
        if x == y:
            return
        self._swap_recursive_helper(self.head, None, x, y)

    def _swap_recursive_helper(self, curr, prev, x, y):
        if not curr:
            return
        
        if curr.data == x:
            x_node = curr
            x_prev = prev
        elif curr.data == y:
            y_node = curr
            y_prev = prev
        
        if x_node and y_node:
            if x_prev:
                x_prev.next = y_node
            else:
                self.head = y_node
            
            if y_prev:
                y_prev.next = x_node
            else:
                self.head = x_node
            
            x_node.next, y_node.next = y_node.next, x_node.next
            return
        
        self._swap_recursive_helper(curr.next, curr, x, y)

    def display(self):
        current = self.head
        if not current:
            print("Lista vazia!")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")