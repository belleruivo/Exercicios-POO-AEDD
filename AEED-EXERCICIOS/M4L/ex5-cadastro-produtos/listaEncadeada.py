from node import Node

class UnorderedLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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