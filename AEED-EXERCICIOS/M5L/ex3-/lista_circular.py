from node import Node

class ListaCircular:
    def __init__(self):
        self.head = None

    # a. Buscar um nome dado o valor da chave
    def buscar(self, chave):
        if self.head is None:
            return None
        temp = self.head
        while True:
            if temp.chave == chave:
                return temp.nome
            temp = temp.next
            if temp == self.head:
                break
        return None

    # b. Inserir um novo elemento na lista mantendo a ordem (FIFO)
    def inserir_fifo(self, chave, nome):
        novo_node = Node(chave, nome)
        if self.head is None:
            novo_node.next = novo_node
            novo_node.prev = novo_node
            self.head = novo_node
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = novo_node
        novo_node.prev = temp
        novo_node.next = self.head
        self.head.prev = novo_node

    # c. Remover um elemento da lista (FIFO)
    def remover_fifo(self):
        if self.head is None:
            return "Lista vazia"
        if self.head.next == self.head:  # Só um nó na lista
            self.head = None
            return "Elemento removido"
        temp = self.head
        self.head = temp.next
        self.head.prev = temp.prev
        temp.prev.next = self.head
        return f"Elemento {temp.nome} removido"

    # d. Imprimir os valores da lista
    def imprimir(self):
        if self.head is None:
            print("Lista vazia")
            return
        temp = self.head
        while True:
            print(f"Chave: {temp.chave}, Nome: {temp.nome}")
            temp = temp.next
            if temp == self.head:
                break

    # e. Copiar uma lista l1 para uma lista l2
    def copiar(self, lista_l2):
        if self.head is None:
            return False
        temp = self.head
        while True:
            lista_l2.inserir_fifo(temp.chave, temp.nome)
            temp = temp.next
            if temp == self.head:
                break
        return True

    # f. Concatenar uma lista l1 com uma lista l2
    def concatenar(self, lista_l2):
        if self.head is None:
            self.head = lista_l2.head
            return
        if lista_l2.head is None:
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = lista_l2.head
        lista_l2.head.prev = temp
        temp = lista_l2.head
        while temp.next != lista_l2.head:
            temp = temp.next
        temp.next = self.head
        self.head.prev = temp

    # g. Intercalar l1 com a lista copiada em l2
    def intercalar(self, lista_l2):
        if self.head is None or lista_l2.head is None:
            return
        
        temp1, temp2 = self.head, lista_l2.head
        nova_lista = ListaCircular()

        while temp1 != self.head or temp2 != lista_l2.head:
            # Intercalar alternadamente entre os elementos de l1 e l2
            if temp1:
                nova_lista.inserir_fifo(temp1.chave, temp1.nome)
                temp1 = temp1.next
                if temp1 == self.head:
                    temp1 = None  # Parar de adicionar de l1 ao chegar no fim

            if temp2:
                nova_lista.inserir_fifo(temp2.chave, temp2.nome)
                temp2 = temp2.next
                if temp2 == lista_l2.head:
                    temp2 = None  # Parar de adicionar de l2 ao chegar no fim

        # Atualizar `self.head` com a lista intercalada
        self.head = nova_lista.head
