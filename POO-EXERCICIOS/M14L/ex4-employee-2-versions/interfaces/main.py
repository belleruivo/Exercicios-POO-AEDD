from manager import Manager
from salesperson import Salesperson
from itrainable import ITrainable
from ilogistics_handler import ILogisticsHandler

'''Essas interfaces garantem que qualquer classe que as implemente terá que cumprir os contratos definidos, permitindo um código mais modular e flexível.'''

def main():
    employees = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Gerente")
        print("2. Adicionar Vendedor")
        print("3. Listar Funcionários")
        print("4. Executar Tarefas Adicionais")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do Gerente: ")
            salary = float(input("Salário: "))
            department = input("Departamento: ")
            manager = Manager(name, salary, department)
            employees.append(manager)
            print("Gerente adicionado com sucesso!")
        elif choice == "2":
            name = input("Nome do Vendedor: ")
            salary = float(input("Salário: "))
            region = input("Região: ")
            salesperson = Salesperson(name, salary, region)
            employees.append(salesperson)
            print("Vendedor adicionado com sucesso!")
        elif choice == "3":
            print("\nLista de Funcionários:")
            for i, employee in enumerate(employees, 1):
                print(f"{i}. {employee}")
        #  as interfaces são usadas para verificar se os objetos implementam funcionalidades adicionais. Isso é feito com a função isinstance.
        # Verificação com isinstance:
        # ITrainable: Verifica se o objeto suporta o método conduct_training.
        # ILogisticsHandler: Verifica se o objeto suporta o método handle_logistics.
        elif choice == "4":
            print("\nExecutando Tarefas Adicionais:")
            for employee in employees:
                if isinstance(employee, ITrainable):
                    print(employee.conduct_training())
                if isinstance(employee, ILogisticsHandler):
                    print(employee.handle_logistics())
        elif choice == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
