'''
Considere, como subclasse da classe Person, a classe Employee. Considere que
cada instância da classe Employee tem, para além dos atributos que caracterizam a
classe Person, os atributos sectorCode (inteiro), baseSalary (vencimento base) e tax
(porcentagem retida dos impostos). Implemente a classe Employee com métodos
seletores e modificadores e um método calculateSalary. Altere o main para que você
possa verificar o funcionamento dos métodos implementados na classe Employee e
os herdados da classe Person.
'''

from person import Person

class Employee(Person):
    def __init__(self, nome, endereco, cpf, rg, telefone, sector_code=0, base_salary=0.0, tax=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.set_sector_code(sector_code)
        self.set_base_salary(base_salary)
        self.set_tax(tax)

    def get_sector_code(self):
        return self.__sector_code

    def get_base_salary(self):
        return self.__base_salary

    def get_tax(self):
        return self.__tax

    def set_sector_code(self, sector_code):
        if isinstance(sector_code, int):
            self.__sector_code = sector_code
        else:
            raise ValueError("Código de setor inválido")

    def set_base_salary(self, base_salary):
        if isinstance(base_salary, (int, float)) and base_salary >= 0:
            self.__base_salary = base_salary
        else:
            raise ValueError("Salário base inválido")

    def set_tax(self, tax):
        if isinstance(tax, (int, float)) and 0 <= tax <= 1:
            self.__tax = tax
        else:
            raise ValueError("Taxa inválida")

    def calculate_salary(self):
        return self.__base_salary * (1 - self.__tax)
