from linked_list import LinkedList

def main():
    lista = LinkedList()
    vetor = []

    while True:
        print("\nMenu:")
        print("1. Inserir números na lista")
        print("2. Copiar vetor para lista (iterativo)")
        print("3. Copiar vetor para lista (recursivo)")
        print("4. Copiar lista para vetor (iterativo)")
        print("5. Copiar lista para vetor (recursivo)")
        print("6. Mostrar lista")
        print("7. Mostrar vetor")
        print("8. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nums = input("Digite os números para inserir na lista, separados por espaços: ")
            for num in map(int, nums.split()):
                lista.insert(num)
        elif opcao == 2:
            vetor = list(map(int, input("Digite os números para o vetor, separados por espaços: ").split()))
            lista.copy_from_array_iterative(vetor)
        elif opcao == 3:
            vetor = list(map(int, input("Digite os números para o vetor, separados por espaços: ").split()))
            lista.copy_from_array_recursive(vetor)
        elif opcao == 4:
            vetor = lista.copy_to_array_iterative()
            print("Vetor copiado da lista (iterativo):", vetor)
        elif opcao == 5:
            vetor = lista.copy_to_array_recursive()
            print("Vetor copiado da lista (recursivo):", vetor)
        elif opcao == 6:
            current = lista.head
            print("Lista:", end=" ")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
        elif opcao == 7:
            print("Vetor:", vetor)
        elif opcao == 8:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()