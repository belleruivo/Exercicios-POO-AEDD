from linked_list import LinkedList

def main():
    lista1 = LinkedList()
    lista2 = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Inserir números na lista 1")
        print("2. Inserir números na lista 2")
        print("3. Encontrar menor valor na lista 1 (iterativo)")
        print("4. Encontrar menor valor na lista 2 (iterativo)")
        print("5. Encontrar menor valor na lista 1 (recursivo)")
        print("6. Encontrar menor valor na lista 2 (recursivo)")
        print("7. Verificar se as listas são iguais (iterativo)")
        print("8. Verificar se as listas são iguais (recursivo)")
        print("9. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nums = input("Digite os números para inserir na lista 1, separados por espaços: ")
            for num in map(int, nums.split()):
                lista1.insert(num)
        elif opcao == 2:
            nums = input("Digite os números para inserir na lista 2, separados por espaços: ")
            for num in map(int, nums.split()):
                lista2.insert(num)
        elif opcao == 3:
            min_value = lista1.find_min_iterative()
            print(f"Menor valor na lista 1 (iterativo): {min_value}")
        elif opcao == 4:
            min_value = lista2.find_min_iterative()
            print(f"Menor valor na lista 2 (iterativo): {min_value}")
        elif opcao == 5:
            min_value = lista1.find_min_recursive()
            print(f"Menor valor na lista 1 (recursivo): {min_value}")
        elif opcao == 6:
            min_value = lista2.find_min_recursive()
            print(f"Menor valor na lista 2 (recursivo): {min_value}")
        elif opcao == 7:
            are_equal = lista1.are_equal_iterative(lista2)
            print(f"As listas são iguais (iterativo)? {'Sim' if are_equal else 'Não'}")
        elif opcao == 8:
            are_equal = lista1.are_equal_recursive(lista1.head, lista2.head)
            print(f"As listas são iguais (recursivo)? {'Sim' if are_equal else 'Não'}")
        elif opcao == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()