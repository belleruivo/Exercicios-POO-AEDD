# employee.py
class Employee:
    def __init__(self, nome: str, sobrenome: str, salario_mensal: float):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_mensal = max(salario_mensal, 0.0)  # garante salário mensal positivo

    @property
    def nome(self) -> str:
        """Obtém o nome do funcionário."""
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        """Define o nome do funcionário, garantindo que não seja vazio."""
        if not value.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = value

    @property
    def sobrenome(self) -> str:
        """Obtém o sobrenome do funcionário."""
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, value: str) -> None:
        """Define o sobrenome do funcionário, garantindo que não seja vazio."""
        if not value.strip():
            raise ValueError("O sobrenome não pode ser vazio.")
        self._sobrenome = value

    @property
    def salario_mensal(self) -> float:
        """Obtém o salário mensal do funcionário."""
        return self._salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, value: float) -> None:
        """Define o salário mensal, garantindo que seja não negativo."""
        self._salario_mensal = max(value, 0.0)

    def salario_anual(self) -> float:
        """Calcula o salário anual do funcionário."""
        return self.salario_mensal * 12

    def dar_aumento(self, porcentagem: float) -> None:
        """Aplica um aumento percentual ao salário mensal."""
        self.salario_mensal *= (1 + porcentagem / 100)
