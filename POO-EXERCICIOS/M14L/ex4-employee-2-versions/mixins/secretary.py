from employee import Employee

class Secretary(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)

    def get_job_description(self):
        return "Secretário que auxilia na administração e coordenação de atividades."

    def __str__(self):
        return f"{super().__str__()} (Secretário)"
