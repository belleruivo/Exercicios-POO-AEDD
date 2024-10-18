# extended_employee.py
from employee import Employee
from typing import Optional

class ExtendedEmployee(Employee):
    def __init__(self, nome: str, sobrenome: str, salario_mensal: float, departamento: Optional[str] = None):
        super().__init__(nome, sobrenome, salario_mensal)
        self.departamento = departamento or "Não especificado"

    @property
    def departamento(self) -> str:
        """Obtém o departamento do funcionário."""
        return self._departamento

    @departamento.setter
    def departamento(self, value: str) -> None:
        """Define o departamento do funcionário, garantindo que não seja vazio."""
        if not value.strip():
            raise ValueError("O departamento não pode ser vazio.")
        self._departamento = value
