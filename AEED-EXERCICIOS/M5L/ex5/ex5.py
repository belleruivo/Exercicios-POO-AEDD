'''5. Escreva um programa que simule o controle de uma pista de decolagem de aviões em
um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes
tarefas:
a. Listar o número de aviões aguardando na fila de decolagem;
b. Autorizar a decolagem do primeiro avião da fila;
c. Adicionar um avião à fila de espera;
d. Listar todos os aviões na fila de espera;
e. Listar as características do primeiro avião da fila.
Considere que os aviões possuem um nome e um número inteiro como identificador.
Adicione outras características conforme achar necessário.'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def enqueue(self, airplane):
        new_node = Node(airplane)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Empty List")
            return None
        removed_airplane = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return removed_airplane

    def peek(self):
        return self.front.data if self.front else None

    def list_airplanes(self):
        current = self.front
        airplanes = []
        while current:
            airplanes.append(current.data)
            current = current.next
        return airplanes


class Airplane:
    def __init__(self, name, id_number, model, manufacturer):
        self.name = name
        self.id_number = id_number
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return f"Avião: {self.name}, ID: {self.id_number}, Modelo: {self.model}, Fabricante: {self.manufacturer}"


def main():
    queue = Queue()

    while True:
        print("\nControle de Pista de Decolagem de Aviões")
        print("1. Listar número de aviões aguardando na fila")
        print("2. Autorizar decolagem do primeiro avião da fila")
        print("3. Adicionar um avião à fila de espera")
        print("4. Listar todos os aviões na fila de espera")
        print("5. Listar características do primeiro avião da fila")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            print(f"Número de aviões aguardando na fila: {queue.size}")

        elif choice == "2":
            airplane = queue.dequeue()
            if airplane:
                print(f"Avião autorizado para decolagem: {airplane.name}")
            else:
                print("Não há aviões na fila.")

        elif choice == "3":
            name = input("Nome do avião: ")
            id_number = int(input("ID do avião: "))
            model = input("Modelo do avião: ")
            manufacturer = input("Fabricante do avião: ")
            airplane = Airplane(name, id_number, model, manufacturer)
            queue.enqueue(airplane)
            print(f"Avião {name} adicionado à fila.")

        elif choice == "4":
            airplanes = queue.list_airplanes()
            if airplanes:
                print("Aviões na fila de espera:")
                for i, airplane in enumerate(airplanes, start=1):
                    print(f"{i}. {airplane}")
            else:
                print("Não há aviões na fila.")

        elif choice == "5":
            airplane = queue.peek()
            if airplane:
                print(f"Características do primeiro avião da fila: {airplane}")
            else:
                print("Não há aviões na fila.")

        elif choice == "0":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
