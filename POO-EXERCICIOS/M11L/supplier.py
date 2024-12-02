'''2. Considere, como subclasse da classe Person, a classe Supplier, para representar um
fornecedor. Considere que cada instância da classe Supplier tem, para além dos
atributos que caracterizam a classe Person, os atributos valueCredit (correspondente
ao crédito máximo atribuído ao fornecedor) e valueDebt (montante da dívida para com
o fornecedor). Implemente na classe Supplier, para além dos usuais métodos
seletores e modificadores, um método getBalance() que devolve a diferença entre os
valores dos atributos valueCredit e valueDebt. Depois de implementada a classe
Supplier, altere o main para que você possa verificar o funcionamento dos métodos
implementados na classe Supplier e os herdados da classe Person.
'''

from person import Person

class Supplier(Person):  # Supplier herda todos os atributos de Person
    def __init__(self, nome, endereco, cpf, rg, telefone, value_credit=0.0, value_debt=0.0):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__value_credit = value_credit
        self.__value_debt = value_debt

    def get_value_credit(self):
        return self.__value_credit

    def get_value_debt(self):
        return self.__value_debt

    def set_value_credit(self, value_credit):
        if isinstance(value_credit, (int, float)) and value_credit >= 0:
            self.__value_credit = value_credit
        else:
            raise ValueError("Valor de crédito inválido")

    def set_value_debt(self, value_debt):
        if isinstance(value_debt, (int, float)) and value_debt >= 0:
            self.__value_debt = value_debt
        else:
            raise ValueError("Valor de dívida inválido")

    def get_balance(self):
        return self.__value_credit - self.__value_debt
