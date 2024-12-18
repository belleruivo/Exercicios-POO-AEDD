'''4. Implemente a classe Administrator como subclasse da classe Employee. Um
determinado administrador tem como atributos, para além dos atributos da classe
Person e da classe Employee, o atributo subsistenceAllowance (ajudas referentes a
viagens, estadias...). Note que deverá redefinir na classe Administrator o método
herdado calculateSalary (o salário de um administrador é equivalente ao salário de
um empregado usual acrescido da ajuda de custo). Altere o main para que você
possa verificar o funcionamento dos métodos implementados na classe
Administrator e os herdados.'''

from employee import Employee

class Administrator(Employee):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax, subsistence_allowance=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone, sector_code, base_salary, tax)
        self.set_subsistence_allowance(subsistence_allowance)

    def get_subsistence_allowance(self):
        return self.__subsistence_allowance

    def set_subsistence_allowance(self, subsistence_allowance):
        if isinstance(subsistence_allowance, (int, float)) and subsistence_allowance >= 0:
            self.__subsistence_allowance = subsistence_allowance
        else:
            raise ValueError("Ajuda de custo inválida")

    def calculate_salary(self):
        return super().calculate_salary() + self.__subsistence_allowance
