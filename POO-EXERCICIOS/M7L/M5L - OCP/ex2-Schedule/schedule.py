# schedule.py
from contact import Contact

class Schedule:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Digite o nome do contato: ")
        phone_number = input("Digite o número de telefone: ")

        if not Contact.is_valid_phone(phone_number):
            print("Número de telefone inválido. Tente novamente.")
            return

        self.contacts[name.lower()] = phone_number  # Armazenando o nome em minúsculas
        print(f"Contato {name} adicionado com sucesso!")

    def edit_contact(self):
        print(f"Contatos: {self.contacts}")
        name = input("Digite o nome do contato que deseja editar: ").lower()  # Convertendo para minúsculas
        if name in self.contacts:
            new_phone_number = input("Digite o novo número de telefone: ")
            if not Contact.is_valid_phone(new_phone_number):
                print("Número de telefone inválido. Tente novamente.")
                return
            self.contacts[name] = new_phone_number
            print(f"Contato {name} editado com sucesso!")
        else:
            print(f"Contato {name} não encontrado.")

    def remove_contact(self):
        print(f"Contatos: {self.contacts}")
        name = input("Digite o nome do contato que deseja remover: ").lower()  # Convertendo para minúsculas
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contato {name} removido com sucesso!")
        else:
            print(f"Contato {name} não encontrado.")

    def search_by_name(self):
        name = input("Digite o nome que deseja buscar: ").lower()  # Convertendo para minúsculas
        print(self.contacts.get(name, "Contato não encontrado."))

    def search_by_phone(self):
        phone_number = input("Digite o número de telefone que deseja buscar: ")
        for name, number in self.contacts.items():
            if number == phone_number:
                print(f"Contato encontrado: {name}")
                return
        print("Número não encontrado.")
