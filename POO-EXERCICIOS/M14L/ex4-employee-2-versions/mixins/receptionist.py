from employee import Employee

class Receptionist(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)

    def get_job_description(self):
        return "Recepcionista que atende aos clientes e organiza a agenda."

    def __str__(self):
        return f"{super().__str__()} (Recepcionista)"
