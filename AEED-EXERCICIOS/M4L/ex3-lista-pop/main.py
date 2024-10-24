'''
Defina uma função chamada pop que remove o item em determinada posição de uma
estrutura unicamente ligada. Essa função espera uma posição como primeiro
argumento, com a precondição 0 <= posição < comprimento da estrutura. Seu
segundo argumento é a estrutura ligada, que, é claro, não pode estar vazia. A função
retorna uma tupla contendo a estrutura ligada modificada e o item que foi removido.
Um exemplo de chamada é (head, item) = pop(1, head).
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next # o próximo nó

def pop(position, head):
    if position == 0: # se a posição for 0, remova o primeiro item
        removed_item = head.data # o item removido é o primeiro
        head = head.next # o novo head é o próximo
        return head, removed_item # retorna o novo head e o item removido

    current = head # se não, percorra a lista até a posição desejada
    for _ in range(position - 1): # percorre a lista até a posição desejada
        if current.next is None: # se o próximo for nulo, a posição está fora dos limites
            raise IndexError("Position out of bounds")
        current = current.next # se não, vá para o próximo

    if current.next is None: # se o próximo for nulo, a posição está fora dos limites
        raise IndexError("Position out of bounds")

    removed_item = current.next.data # o item removido é o próximo
    current.next = current.next.next # o próximo é o próximo do próximo
    return head, removed_item # retorna o novo head e o item removido

# Exemplo de uso
if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4)))) # cria uma lista ligada
    head, item = pop(1, head) # remove o item na posição 1
    print(f"Item removido: {item}")  # Output: 2
    current = head # imprime a lista ligada
    while current: # enquanto houver um nó
        print(current.data, end=" -> ") # imprime o dado do nó
        current = current.next # vá para o próximo
    print("None")  # Output: 1 -> 3 -> 4 -> None