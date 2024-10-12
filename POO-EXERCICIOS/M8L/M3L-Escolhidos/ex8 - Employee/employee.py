from salary_manager import SalaryManager  # Importa a classe SalaryManager

class Employee:
    def __init__(self, nome, sobrenome, salary_manager: SalaryManager):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salary_manager = salary_manager

    def salario_anual(self):
        return self.salary_manager.calcular_salario_anual()  # Método para calcular o salário anual

    def dar_aumento(self, porcentagem):
        self.salary_manager.dar_aumento(porcentagem)  # Método para dar um aumento
