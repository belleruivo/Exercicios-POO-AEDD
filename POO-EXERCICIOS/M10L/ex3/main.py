# main.py

from employee import Employee

def display_menu():
    print("\nMenu:")
    print("1. Adicionar Funcionário")
    print("2. Visualizar Funcionários")
    print("3. Calcular Salário")
    print("4. Sair")

def main():
    employees = []  # Lista para armazenar funcionários
    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            # Adicionar Funcionário
            try:
                name = input("Digite o nome do funcionário: ")
                age = int(input("Digite a idade do funcionário: "))
                sector_code = int(input("Digite o código do setor: "))
                base_salary = float(input("Digite o salário base: "))
                tax = float(input("Digite a porcentagem de imposto: "))
                
                if age < 0 or base_salary < 0 or tax < 0:
                    raise ValueError("Idade, salário e taxa não podem ser negativos.")
                
                employee = Employee(name, age, sector_code, base_salary, tax)
                employees.append(employee)
                print(f"Funcionário {name} adicionado com sucesso.")
            except ValueError as e:
                print(f"Erro ao adicionar funcionário: {e}")
            except Exception as e:
                print(f"Um erro inesperado ocorreu: {e}")

        elif choice == '2':
            # Visualizar Funcionários
            if not employees:
                print("Nenhum funcionário cadastrado.")
            else:
                print("\nFuncionários cadastrados:")
                for idx, emp in enumerate(employees):
                    print(f"{idx + 1}. {emp}")  # Exibe o índice começando de 1

        elif choice == '3':
            # Calcular Salário
            if not employees:
                print("Nenhum funcionário cadastrado.")
            else:
                # Exibir funcionários antes de calcular o salário
                print("\nFuncionários cadastrados:")
                for idx, emp in enumerate(employees):
                    print(f"{idx + 1}. {emp}")  # Exibe o índice começando de 1
                
                try:
                    employee_index = int(input("Digite o número do funcionário para calcular o salário: ")) - 1
                    if 0 <= employee_index < len(employees):
                        employee = employees[employee_index]
                        salary = employee.calculate_salary()
                        print(f"O salário calculado para {employee.get_name()} é: {salary:.2f}")
                    else:
                        print("Número de funcionário inválido. Por favor, insira um número entre 1 e {}.".format(len(employees)))
                except ValueError:
                    print("Por favor, insira um número válido.")
                except Exception as e:
                    print(f"Um erro inesperado ocorreu: {e}")

        elif choice == '4':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
