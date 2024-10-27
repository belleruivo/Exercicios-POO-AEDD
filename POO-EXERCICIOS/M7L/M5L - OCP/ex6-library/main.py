'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

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


# Você criou subclasses como AddBookAction, BorrowBookAction, CheckAvailabilityAction e ReturnBookAction, todas herdando de LibraryAction. Cada uma dessas classes implementa o método execute() de maneira específica. Isso demonstra que, para adicionar novas funcionalidades à biblioteca (como, por exemplo, a ação de remover um livro), você pode criar uma nova classe de ação sem precisar alterar as classes existentes.
# ou seja, seria so adicionar no dicionario do mainw