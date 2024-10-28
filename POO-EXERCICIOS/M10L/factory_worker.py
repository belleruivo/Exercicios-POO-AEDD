from employee import Employee

class FactoryWorker(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_production, commission):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.value_production = value_production
        self.commission = commission

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        commission_amount = (self.value_production * self.commission) / 100
        return base_salary + commission_amount

    def get_value_production(self):
        return self.value_production

    def get_commission(self):
        return self.commission
