from node import Node

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_end(self, funcionario):
        new_node = Node(funcionario)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            new_node.previous = new_node
        else:
            new_node.previous = self.head.previous
            new_node.next = self.head
            self.head.previous.next = new_node
            self.head.previous = new_node

    def insert_front(self, funcionario):
        new_node = Node(funcionario)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
            new_node.previous = new_node
        else:
            new_node.next = self.head
            new_node.previous = self.head.previous
            self.head.previous.next = new_node
            self.head.previous = new_node
            self.head = new_node
            
    def inserir_ordenado(self, funcionario):
        if self.is_empty() or funcionario.salario < self.head.funcionario.salario:
            self.insert_front(funcionario)
        else:
            current = self.head
            while True:
                if funcionario.salario < current.funcionario.salario:
                    new_node = Node(funcionario)
                    new_node.next = current
                    new_node.previous = current.previous
                    current.previous.next = new_node
                    current.previous = new_node
                    break
                elif current.next == self.head:  # Inserindo no final
                    self.insert_end(funcionario)
                    break
                current = current.next

    def calcular_imposto(self):
        info = []
        current = self.head
        while True:
            salario = current.funcionario.salario
            if salario <= 850:
                imposto = 0
            elif 850 < salario <= 1200:
                imposto = salario * 0.10
            else:
                imposto = salario * 0.20
            
            valor_a_receber = salario - imposto
            info.append((current.funcionario.nome, imposto, valor_a_receber))

            current = current.next
            if current == self.head:
                break
        return info

    def show_by_initial(self, initial):
        current = self.head
        found = False
        while True:
            if current.funcionario.nome.lower().startswith(initial.lower()):
                print(f"Nome: {current.funcionario.nome}, Salário: R${current.funcionario.salario:.2f}")
                found = True

            current = current.next
            if current == self.head:
                break
        
        if not found:
            print("Nenhum funcionário encontrado com essa letra inicial.")

    def print_list(self, reverse=False):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        if reverse:
            current = self.head.previous
            while True:
                print(f"Nome: {current.funcionario.nome}, Salário: R${current.funcionario.salario:.2f}")
                current = current.previous
                if current == self.head.previous:
                    break
        else:
            current = self.head
            while True:
                print(f"Nome: {current.funcionario.nome}, Salário: R${current.funcionario.salario:.2f}")
                current = current.next
                if current == self.head:
                    break
