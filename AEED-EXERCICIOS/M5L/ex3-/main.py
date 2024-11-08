from lista_circular import ListaCircular

def main():
    lista1 = ListaCircular()
    lista2 = ListaCircular()

    while True:
        print("\nEscolha uma operação:")
        print("1. Inserir elemento na lista 1")
        print("2. Buscar elemento na lista 1")
        print("3. Remover elemento da lista 1")
        print("4. Imprimir lista 1")
        print("5. Copiar lista 1 para lista 2")
        print("6. Concatenar lista 1 com lista 2")
        print("7. Intercalar lista 1 e lista 2")
        print("8. Imprimir lista 2")
        print("9. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            chave = int(input("Digite a chave para a lista 1: "))
            nome = input("Digite o nome para a lista 1: ")
            lista1.inserir_fifo(chave, nome)
            print(f"Elemento ({chave}, {nome}) inserido na lista 1.")
        
        elif opcao == '2':
            chave = int(input("Digite a chave para buscar na lista 1: "))
            resultado = lista1.buscar(chave)
            if resultado:
                print(f"Nome encontrado: {resultado}")
            else:
                print("Chave não encontrada na lista 1.")
        
        elif opcao == '3':
            print(lista1.remover_fifo())
        
        elif opcao == '4':
            print("Elementos da lista 1:")
            lista1.imprimir()
        
        elif opcao == '5':
            lista1.copiar(lista2)
            print("Lista 1 copiada para lista 2.")
        
        elif opcao == '6':
            lista1.concatenar(lista2)
            print("Lista 1 concatenada com lista 2.")
        
        elif opcao == '7':
            lista1.intercalar(lista2)
            print("Listas 1 e 2 intercaladas em lista 1.")
        
        elif opcao == '8':
            print("Elementos da lista 2:")
            lista2.imprimir()
        
        elif opcao == '9':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
