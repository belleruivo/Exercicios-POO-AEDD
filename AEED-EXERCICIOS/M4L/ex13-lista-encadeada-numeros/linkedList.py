from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def insertAfter(self, k, new_data):
        current = self.head
        count = 1
        
        while current and count < k:
            current = current.next
            count += 1
        
        if not current:
            print("A posição k fornecida não existe na lista.")
            return

        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node
    
    def swap_iterative(self, x, y):
        if x == y:
            return

        prev_x, curr_x = None, self.head
        while curr_x and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next

        prev_y, curr_y = None, self.head
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
        self._swap_recursive_helper(self.head, None, None, None, x, y)

    def _swap_recursive_helper(self, curr, prev, x_node, y_node, x_prev, y_prev, x, y):
        if not curr:
            return

        if curr.data == x:
            x_node, x_prev = curr, prev
        elif curr.data == y:
            y_node, y_prev = curr, prev


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

        self._swap_recursive_helper(curr.next, curr, x_node, y_node, x, y)

    def display(self):
        if self.isEmpty():
            print("Lista vazia!")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")