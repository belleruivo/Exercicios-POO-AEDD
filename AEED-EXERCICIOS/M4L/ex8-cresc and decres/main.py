from listas import insert_singly_linked, insert_doubly_linked_sorted, print_doubly_linked, print_doubly_linked_reverse

def main():
    n = int(input("Digite o número de elementos: "))
    
    # Inicializando as listas
    even_list = None   # Lista de números pares
    odd_list = None    # Lista de números ímpares
    sorted_list = None # Lista duplamente encadeada e ordenada
    
    # Receber n números e distribuí-los entre pares e ímpares
    for _ in range(n):
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            even_list = insert_singly_linked(even_list, num)
        else:
            odd_list = insert_singly_linked(odd_list, num)
    
    # Inserir os números das duas listas (pares e ímpares) na lista duplamente encadeada e ordenada
    current = even_list
    while current:
        sorted_list = insert_doubly_linked_sorted(sorted_list, current.data)
        current = current.next
    current = odd_list
    while current:
        sorted_list = insert_doubly_linked_sorted(sorted_list, current.data)
        current = current.next
    
    # Exibir a lista duplamente encadeada
    print("Lista em ordem crescente:")
    print_doubly_linked(sorted_list)
    
    print("Lista em ordem decrescente:")
    print_doubly_linked_reverse(sorted_list)

if __name__ == "__main__":
    main()
