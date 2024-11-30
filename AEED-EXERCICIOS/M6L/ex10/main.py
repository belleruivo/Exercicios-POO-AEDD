# 10. Adicione o método rebalance a uma Árvore Binária de Busca. O método copia os itens
# da árvore para uma lista durante um percurso em in-ordem e, em seguida, limpa a
# árvore. O método então copia os itens da lista de volta para a árvore de tal maneira
# que a forma da árvore permaneça balanceada. Dica: Use uma função auxiliar
# recursiva que visite repetidamente os itens nos pontos médios das partes da lista.

# main.py
from binary_tree import BinaryTree

def menu():
    tree = BinaryTree()
    
    while True:
        print("\nMenu:")
        print("1 - Inserir número")
        print("2 - Mostrar se a árvore é estritamente binária")
        print("3 - Mostrar se a árvore é completa")
        print("4 - Mostrar se a árvore é cheia")
        print("5 - Rebalancear a árvore")
        print("6 - Imprimir a árvore")
        print("7 - Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            value = int(input("Digite um número para inserir: "))
            tree.insert(value)
        
        elif choice == '2':
            if tree.is_strictly_binary():
                print("A árvore é estritamente binária.")
            else:
                print("A árvore não é estritamente binária.")
        
        elif choice == '3':
            if tree.is_complete():
                print("A árvore é completa.")
            else:
                print("A árvore não é completa.")
        
        elif choice == '4':
            if tree.is_full():
                print("A árvore é cheia.")
            else:
                print("A árvore não é cheia.")
        
        elif choice == '5':
            tree.rebalance()
        
        elif choice == '6':
            tree.print_tree()
        
        elif choice == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
