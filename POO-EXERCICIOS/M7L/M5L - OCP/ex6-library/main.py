from Library import Library
from AddBookAction import AddBookAction
from BorrowBookAction import BorrowBookAction
from ReturnBookAction import ReturnBookAction
from CheckAvailabilityAction import CheckAvailabilityAction

def main():
    library = Library()
    actions = {
        '1': AddBookAction(library),
        '2': BorrowBookAction(library),
        '3': ReturnBookAction(library),
        '4': CheckAvailabilityAction(library),
    }

    while True:
        print("\n1. Cadastrar livro")
        print("2. Fazer empréstimo")
        print("3. Devolver livro")
        print("4. Verificar disponibilidade")
        print("5. Sair")

        choice = input("Escolha uma opção: ").strip()

        if choice in actions:
            actions[choice].execute()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
