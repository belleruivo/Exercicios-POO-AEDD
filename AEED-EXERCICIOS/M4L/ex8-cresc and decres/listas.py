from node import Node

# Função para inserir um número na lista simplesmente encadeada (no final)
def insert_singly_linked(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

# Função para inserir um número na lista duplamente encadeada, mantendo a ordem crescente
def insert_doubly_linked_sorted(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    # Se o novo nó for menor que o primeiro nó
    if data < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    current = head
    while current.next and current.data < data:
        current = current.next
    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    return head

# Função para imprimir a lista duplamente encadeada (crescente)
def print_doubly_linked(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Função para imprimir a lista duplamente encadeada (decrescente)
def print_doubly_linked_reverse(head):
    current = head
    if not current:
        return
    while current.next:
        current = current.next
    while current:
        print(current.data, end=" ")
        current = current.prev
    print()
