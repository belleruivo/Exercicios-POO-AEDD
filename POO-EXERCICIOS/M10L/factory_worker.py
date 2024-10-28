'''5. Implemente a classe FactoryWorker como subclasse da classe Employee. Um
determinado operário tem como atributos, para além dos atributos da classe Person e
da classe Employee, o atributo valueProduction (que corresponde ao valor monetário
dos artigos efetivamente produzidos pelo operário) e commission (que corresponde à
porcentagem do valueProduction que será adicionado ao vencimento base do
operário). Note que deverá redefinir nesta subclasse o método herdado
calculateSalary (o salário de um operário é equivalente ao salário de um empregado
usual acrescido da referida comissão). Altere o main para que você possa verificar o
funcionamento dos métodos implementados na classe FactoryWorker e os herdados.
from employee import Employee'''

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
