from node import Node  # importando a classe Node

def pop(position, head):
    if position == 0:  # se a posição for 0, remova o primeiro item
        removed_item = head.data  # o item removido é o primeiro
        head = head.next  # o novo head é o próximo
        return head, removed_item  # retorna o novo head e o item removido

    current = head  # se não, percorra a lista até a posição desejada
    for _ in range(position - 1):  # percorre a lista até a posição desejada
        if current.next is None:  # se o próximo for nulo, a posição está fora dos limites
            raise IndexError("Position out of bounds")
        current = current.next  # se não, vá para o próximo

    if current.next is None:  # se o próximo for nulo, a posição está fora dos limites
        raise IndexError("Position out of bounds")

    removed_item = current.next.data  # o item removido é o próximo
    current.next = current.next.next  # o próximo é o próximo do próximo
    return head, removed_item  # retorna o novo head e o item removido