'''1. Implemente a classe Employee com nome, número de matrícula e salário.
a. Crie um método para exibir os dados.
b. Crie as classes AdministrativeAssistant e TecnicalAssistent, herdando de
Employee.
c. Sabendo que os assistentes técnicos possuem um bônus salarial e que os
assistentes administrativos possuem um turno (dia ou noite) e um adicional
noturno, sobrescreva o método que exibe os dados.'''


class Employee:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario


    def __str__(self): #representar o objeto como uma string
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Salário: R${self.salario:.2f}"
   
class AdministrativeAssistant(Employee):
    def __init__(self, nome, matricula, salario, turno, adicional_noturno):
        super().__init__(nome, matricula, salario)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def salario_total(self):
        return self.salario + self.adicional_noturno

    def __str__(self):
        return (f"Nome: {self.nome}, Matricula: {self.matricula}, Salário: {self.salario}, "
                f"Turno: {self.turno}, Adicional Noturno: R${self.adicional_noturno:.2f}, Salário Total: R${self.salario_total():.2f}")

class TecnicalAssistant(Employee):
    def __init__(self, nome, matricula, salario, bonus_salarial):
        super().__init__(nome, matricula, salario)
        self.bonus_salarial = bonus_salarial

    def salario_total(self):
        return self.salario + self.bonus_salarial

    def __str__(self):
        return (f"Nome: {self.nome}, Matricula: {self.matricula}, Salário: {self.salario}, "
                f"Bônus Salarial: {self.bonus_salarial:.2f}, Salário Total: R${self.salario_total():.2f}")



