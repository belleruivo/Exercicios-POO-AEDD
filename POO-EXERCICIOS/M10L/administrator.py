# administrator.py
from employee import Employee

class Administrator(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.subsistence_allowance = subsistence_allowance

    def calculate_salary(self):
        # O salário é o salário base menos os impostos mais a ajuda de custo
        return super().calculate_salary() + self.subsistence_allowance

    def get_subsistence_allowance(self):
        return self.subsistence_allowance
