from node import Node

def makeTwoWay(head):
    # Se a lista original estiver vazia, retorna None
    if not head:
        return None
    
    # Criando o primeiro nó da nova lista duplamente ligada
    new_head = Node(head.data)
    current_old = head.next
    current_new = new_head
    
    # O primeiro nó da nova lista duplamente ligada tem o prev como None
    new_head.prev = None
    
    # Percorrendo a lista original
    while current_old:
        # Criando um novo nó para a lista duplamente ligada
        new_node = Node(current_old.data)
        
        # Conectando o nó anterior ao novo nó
        current_new.next = new_node
        new_node.prev = current_new
        
        # Atualizando o ponteiro do nó atual da lista duplamente ligada
        current_new = new_node
        current_old = current_old.next
    
    # Retorna a cabeça da nova lista duplamente ligada
    return new_head
