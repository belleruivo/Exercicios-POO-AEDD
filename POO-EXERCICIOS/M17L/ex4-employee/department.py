# department.py
from employee import Employee

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_employees(self):
        return self.employees

    def __str__(self):
        return f"Department: {self.name}, Employees: {len(self.employees)}"