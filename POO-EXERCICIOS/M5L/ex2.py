'''
Implemente uma classe chamada Schedule que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.
'''

class Schedule:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Digite o nome do contato: ")
        phone_number = input("Digite o número de telefone: ")

        if not self.is_valid_phone(phone_number):
            print("Número de telefone inválido. Tente novamente.")
            return

        self.contacts[name] = phone_number
        print(f"Contato {name} adicionado com sucesso!")

    def edit_contact(self):
        print(f"Contatos: {self.contacts}")
        name = input("Digite o nome do contato que deseja editar: ")
        if name in self.contacts:
            new_phone_number = input("Digite o novo número de telefone: ")
            if not self.is_valid_phone(new_phone_number):
                print("Número de telefone inválido. Tente novamente.")
                return
            self.contacts[name] = new_phone_number
            print(f"Contato {name} editado com sucesso!")
        else:
            print(f"Contato {name} não encontrado.")

    def remove_contact(self):
        print(f"Contatos: {self.contacts}")
        name = input("Digite o nome do contato que deseja remover: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contato {name} removido com sucesso!")
        else:
            print(f"Contato {name} não encontrado.")

    def search_by_name(self):
        name = input("Digite o nome que deseja buscar: ")
        print(self.contacts.get(name, "Contato não encontrado."))

    def search_by_phone(self):
        phone_number = input("Digite o número de telefone que deseja buscar: ")
        for name, number in self.contacts.items():
            if number == phone_number:
                print(f"Contato encontrado: {name}")
                return
        print("Número não encontrado.")

    @staticmethod
    def is_valid_phone(phone_number):
        return phone_number.isdigit() and (len(phone_number) == 10 or len(phone_number) == 11)


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
