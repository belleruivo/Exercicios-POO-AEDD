class Person:
    def __init__(self, name, address, payment):
        self.name = name
        self.address = address
        self.payment = payment
        self.contacts = [] 
        
    def doPayment(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses")
    
''' O polimorfismo ocorre quando o método doPayment() 
é implementado de forma diferente nas subclasses PhysicalPerson e 
LegalPerson, permitindo que o mesmo método se comporte de 
maneira distinta para cada tipo de objeto'''
    
class PhysicalPerson(Person):
    def __init__(self, name, address, payment, cpf):
        super().__init__(name, address, payment)
        self.cpf = cpf
        self.tax = 0.10
        
    def doPayment(self):
        imposto = self.payment * self.tax
        return self.payment - imposto


class LegalPerson(Person):
    def __init__(self, name, address, payment, cpf, fantasyName, socialReason):
        super().__init__(name, address, payment)
        self.cpf = cpf
        self.fantasyName = fantasyName
        self.socialReason = socialReason
        self.tax = 0.20

    def doPayment(self):
        imposto = self.payment * self.tax
        return self.payment - imposto

