# main.py
from schedule import Schedule

def main():
    agenda = Schedule()

    while True:
        print("\n--- MENU DA AGENDA ---")
        print("1. Adicionar contato")
        print("2. Editar contato")
        print("3. Remover contato")
        print("4. Buscar contato por nome")
        print("5. Buscar contato por telefone")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            agenda.add_contact()
        elif choice == '2':
            agenda.edit_contact()
        elif choice == '3':
            agenda.remove_contact()
        elif choice == '4':
            agenda.search_by_name()
        elif choice == '5':
            agenda.search_by_phone()
        elif choice == '6':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
