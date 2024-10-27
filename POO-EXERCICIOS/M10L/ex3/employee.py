from person import Person

class Employee(Person):
    def __init__(self, name: str, age: int, sector_code: int, base_salary: float, tax: float):
        super().__init__(name, age)
        self._sector_code = sector_code
        self._base_salary = base_salary
        self._tax = tax

    def get_sector_code(self) -> int:
        return self._sector_code

    def set_sector_code(self, sector_code: int):
        self._sector_code = sector_code

    def get_base_salary(self) -> float:
        return self._base_salary

    def set_base_salary(self, base_salary: float):
        self._base_salary = base_salary

    def get_tax(self) -> float:
        return self._tax

    def set_tax(self, tax: float):
        self._tax = tax

    def calculate_salary(self) -> float:
        return self._base_salary * (1 - self._tax / 100)

    def __str__(self):
        return f'{super().__str__()}, Sector Code: {self._sector_code}, Base Salary: {self._base_salary}, Tax: {self._tax}'
