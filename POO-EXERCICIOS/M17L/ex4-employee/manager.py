from employee import Employee

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_job_description(self):
        return f"Manager of {self.department} department."

    def __str__(self):
        return f"{super().__str__()} (Manager - {self.department})"
