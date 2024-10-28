from employee import Employee

class Seller(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.value_sales = value_sales
        self.commission = commission

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        commission_amount = (self.value_sales * self.commission) / 100
        return base_salary + commission_amount

    def get_value_sales(self):
        return self.value_sales

    def get_commission(self):
        return self.commission
