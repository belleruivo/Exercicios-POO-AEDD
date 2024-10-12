from employee import Employee

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, nome, sobrenome, salario_mensal):
        employee = Employee(nome, sobrenome, salario_mensal)
        self.employees.append(employee)
        print(f"Funcionário {nome} {sobrenome} adicionado com sucesso!")

    def display_all_employees(self):
        if not self.employees:
            print("Nenhum funcionário cadastrado.")
        else:
            print("\n--- Lista de Funcionários ---")
            for employee in self.employees:
                print(f"{employee.nome} {employee.sobrenome}: Salário Anual: R${employee.salario_anual():.2f}")

    def give_raise_to_all(self, porcentagem):
        for employee in self.employees:
            employee.dar_aumento(porcentagem)
        print(f"Aumento de {porcentagem}% aplicado a todos os funcionários.")
