from node import Node

class LinkedList:
    def __init__(self):
        self.head = None  # inicializa a lista ligada vazia

    def insert(self, site_name, link):
        new_node = Node(site_name, link)  # cria um novo nó
        new_node.next = self.head  # o novo nó aponta para o nó atual da cabeça
        self.head = new_node  # atualiza a cabeça da lista

    def search_and_move_to_front(self, site_name):
        if self.head is None:  # verifica se a lista está vazia
            return None  # não há itens para buscar

        # caso especial: se o primeiro nó já é o que estamos buscando
        if self.head.site_name == site_name:
            return self.head.link  # retorna o link se encontrado na cabeça

        current = self.head
        previous = None

        while current is not None:
            if current.site_name == site_name:  # se o site for encontrado
                if previous is not None:
                    previous.next = current.next  # remove o nó da sua posição atual
                    current.next = self.head  # o nó se torna a nova cabeça
                    self.head = current  # atualiza a cabeça
                return current.link  # retorna o link do site encontrado
            previous = current
            current = current.next

        return None  # se o site não for encontrado

    def display(self):
        current = self.head
        while current:
            print(f"{current.site_name}: {current.link}")
            current = current.next
