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
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, value_sales=0.0, commission=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.set_value_sales(value_sales)
        self.set_commission(commission)

    def get_value_sales(self):
        return self.__value_sales

    def get_commission(self):
        return self.__commission

    def set_value_sales(self, value_sales):
        if isinstance(value_sales, (int, float)) and value_sales >= 0:
            self.__value_sales = value_sales
        else:
            raise ValueError("Valor de vendas inválido")

    def set_commission(self, commission):
        if isinstance(commission, (int, float)) and 0 <= commission <= 1:
            self.__commission = commission
        else:
            raise ValueError("Comissão inválida")

    def calculate_salary(self):
        return super().calculate_salary() + (self.__value_sales * self.__commission)
