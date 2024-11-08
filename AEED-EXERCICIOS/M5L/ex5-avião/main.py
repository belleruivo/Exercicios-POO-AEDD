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

from queue import Queue
from airplane import Airplane

def main():
    queue = Queue()  # Cria uma instância da fila.

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
            airplane = queue.dequeue()  # Remove o primeiro avião da fila
            if airplane:
                print(f"Avião autorizado para decolagem: {airplane.name}")
                if queue.is_empty():
                    print("Não há mais aviões na fila.")
            else:
                print("Não há aviões na fila para autorizar a decolagem.")

        elif choice == "3":
            name = input("Nome do avião: ")
            id_number = input("ID do avião: ")
            while not id_number.isdigit():  # Verifica se o ID é um número inteiro.
                print("ID inválido. Por favor, insira um número inteiro.")
                id_number = input("ID do avião: ")
            id_number = int(id_number)
            model = input("Modelo do avião: ")
            manufacturer = input("Fabricante do avião: ")
            airplane = Airplane(name, id_number, model, manufacturer)
            queue.enqueue(airplane)  # Adiciona o avião à fila.
            print(f"Avião {name} adicionado à fila.")

        elif choice == "4":
            airplanes = queue.list_airplanes()  # Lista todos os aviões.
            if airplanes:
                print("Aviões na fila de espera:")
                for i, airplane in enumerate(airplanes, start=1):
                    print(f"{i}. {airplane}")
            else:
                print("Não há aviões na fila.")

        elif choice == "5":
            airplane = queue.peek()  # Exibe as informações do primeiro avião.
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