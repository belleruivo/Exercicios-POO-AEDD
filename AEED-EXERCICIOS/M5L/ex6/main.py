from linked_list import LinkedList
from process import process_linked_list

def main():
    linked_list = LinkedList()

    # Entrada de dados do usuário
    input_chars = input("Digite uma sequência alternada de letras e dígitos separados por espaço: ").split()

    # Adiciona caracteres à lista encadeada
    for char in input_chars:
        linked_list.append(char)

    # Processa a lista encadeada
    result = process_linked_list(linked_list)

    # Exibe o resultado
    print("Resultado:", ' '.join(result))

if __name__ == "__main__":
    main()
