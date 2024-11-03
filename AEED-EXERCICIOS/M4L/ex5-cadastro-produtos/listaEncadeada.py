from node import Node

class UnorderedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False
        
    def append(self, new_data):
        new_node = Node(new_data)

        if self.isEmpty():
            self.head = new_node
            self.tail= new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def apply_discount(self, discount_rate):
        current = self.head
        while current:
            current.data['preco'] *= (1 - discount_rate / 100)
            current = current.next

    def report(self):
        current = self.head
        report_data = []
        count_above_500 = 0
        
        while current:
            product = current.data
            report_data.append(f"Código: {product['codigo']}, Novo Preço: {product['preco']:.2f}")
            if product['quantidade'] > 500:
                count_above_500 += 1
            current = current.next
        
        print("\nRelatório de Produtos:")
        for line in report_data:
            print(line)
        print(f"\nQuantidade de produtos com estoque acima de 500: {count_above_500}")