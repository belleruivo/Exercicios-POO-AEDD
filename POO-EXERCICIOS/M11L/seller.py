'''6. Implemente a classe Seller como subclasse da classe Employee. Um determinado
vendedor tem como atributos, para além dos atributos da classe Person e da classe
Employee, o atributo valueSales (correspondente ao valor monetário dos artigos
vendidos) e o atributo commission (porcentagem do valueSales que será adicionado
ao vencimento base do Seller). Note que deverá redefinir nesta subclasse o método
herdado calculateSalary (o salário de um vendedor é equivalente ao salário de um
empregado usual acrescido da referida comissão). Altere o main para que você possa
verificar o funcionamento dos métodos implementados na classe Seller e os
herdados.'''

from employee import Employee

class Seller(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales, commission):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.value_sales = value_sales
        self.commission = commission

    def calculate_salary(self):
        base_salary = super().get_base_salary() * (1 - super().get_tax() / 100)
        commission_amount = (self.value_sales * self.commission) / 100
        return base_salary + commission_amount
