from doubly_linked_list import DoublyLinkedList

def menu():
    print("\n1 - Inserir número na lista")
    print("2 - Imprimir lista")
    print("3 - Inserir após um nó (Iterativo)")
    print("4 - Inserir após um nó (Recursivo)")
    print("5 - Remover nó (Iterativo)")
    print("6 - Remover nó (Recursivo)")
    print("0 - Sair")

def main():
    lista = DoublyLinkedList()

    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            num = int(input("Digite um número para a lista: "))
            lista.insert_front(num)

        elif opcao == 2:
            print("Lista: ", end="")
            lista.print_list()

        elif opcao == 3:
            pos = int(input("Digite o número do nó após o qual deseja inserir: "))
            node = lista.head
            while node and node.data != pos:
                node = node.next
            if node:
                num = int(input("Digite o número a ser inserido: "))
                lista.insert_after(node, num)
            else:
                print("Nó não encontrado.")

        elif opcao == 4:
            pos = int(input("Digite o número do nó após o qual deseja inserir: "))
            node = lista.head
            while node and node.data != pos:
                node = node.next
            if node:
                num = int(input("Digite o número a ser inserido: "))
                lista.insert_after_recursive(node, num)
            else:
                print("Nó não encontrado.")

        elif opcao == 5:
            pos = int(input("Digite o número do nó a ser removido: "))
            node = lista.head
            while node and node.data != pos:
                node = node.next
            if node:
                lista.remove(node)
                print(f"Nó {pos} removido.")
            else:
                print("Nó não encontrado.")

        elif opcao == 6:
            pos = int(input("Digite o número do nó a ser removido: "))
            node = lista.head
            while node and node.data != pos:
                node = node.next
            if node:
                lista.remove_recursive(node)
                print(f"Nó {pos} removido.")
            else:
                print("Nó não encontrado.")

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
