# Defina uma função chamada insert que insere um item em uma estrutura unicamente
# ligada em determinada posição. A função espera três argumentos: o item, a posição e
# a estrutura ligada. (A última pode estar vazia.) A função retorna a estrutura ligada
# modificada. Se a posição é maior ou igual ao comprimento da estrutura, a função
# insere o item no final. Um exemplo de chamada da função, onde head é uma variável
# que é uma ligação vazia ou se refere ao primeiro nó de uma estrutura, é head =
# insert(1, data, head).

from node import Node

def insert(item, position, head):
    new_node = Node(item)

    # Se a posição for 0 ou a lista estiver vazia, insere no início
    if position <= 0 or not head:
        new_node.next = head  # O novo nó aponta para o que era o primeiro nó
        return new_node  # O novo nó se torna o novo "head" da lista

    # Caso contrário, percorre a lista até a posição desejada
    current = head
    current_position = 0
    
    while current is not None and current_position < position - 1:
        current = current.next
        current_position += 1

    # Se o current for None, isso significa que a posição está além do fim da lista
    # Portanto, o item deve ser inserido no final
    if current is None:
        return head  # Não faz nada se a posição for maior que o comprimento da lista

    # Insere o novo nó após o nó atual
    new_node.next = current.next
    current.next = new_node

    return head  # Retorna a cabeça (inicial) da lista

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = None  # Lista inicialmente vazia

head = insert(1, 0, head)  
head = insert(2, 1, head)  
head = insert(3, 2, head)  
head = insert(4, 1, head) 

print_list(head)
