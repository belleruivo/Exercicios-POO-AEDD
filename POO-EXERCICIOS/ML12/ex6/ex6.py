class Person:
    def __init__(self, name, address, payment):
        self.name = name
        self.address = address
        self.payment = payment
        self.contacts = [] 
        
    def doPayment(self, imposto):
        return self.payment - imposto
    
class PhysicalPerson(Person):
    def __init__(self, name, address, payment, cpf, tax):
        super().__init__(name, address, payment)
        self.cpf = cpf
        self.tax = tax
        
    def doPayment(self, imposto):