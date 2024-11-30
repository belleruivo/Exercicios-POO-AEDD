from employee import Employee

class Salesperson(Employee):
    def __init__(self, name: str, salary: float, region: str):
        super().__init__(name, salary)
        self.region = region

    def get_job_description(self):
        return f"Salesperson responsible for the {self.region} region."
    
    '''se eu retirasse o get_job_description: TypeError: Can't instantiate abstract class Salesperson with abstract methods get_job_description'''
    ''' Se uma subclasse não implementa todos os métodos abstratos da classe base, ela também é tratada como abstrata e não pode ser instanciada.'''

    def __str__(self):
        return f"{super().__str__()} (Salesperson - {self.region})"
