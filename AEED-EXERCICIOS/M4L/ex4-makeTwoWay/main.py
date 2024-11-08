from node import Node
from make_two_way import makeTwoWay

# Função para imprimir uma lista unicamente ligada
def print_single_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

# Função para imprimir uma lista duplamente ligada
def print_double_linked_list(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "")
        current = current.next
    print()

def create_single_linked_list():
    head = None
    size = int(input("Quantos elementos deseja adicionar à lista unicamente ligada? "))
    
    for i in range(size):
        data = int(input(f"Digite o {i + 1}º valor: "))
        new_node = Node(data)
        
        # Inserir na lista
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
    
    return head

def main():
    print("Criando lista unicamente ligada...")
    head = create_single_linked_list()
    
    print("\nLista unicamente ligada:")
    print_single_linked_list(head)
    
    print("\nConvertendo para lista duplamente ligada...")
    new_head = makeTwoWay(head)
    
    print("\nLista duplamente ligada:")
    print_double_linked_list(new_head)

if __name__ == "__main__":
    main()
