'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

from typing import Optional

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

def main():
    # Criando dois objetos Employee
    emp1 = ExtendedEmployee("Murilo", "Dantas", 3000.0, "TI")
    emp2 = ExtendedEmployee("Pedro", "Henrique", 2500.0, "RH")

    # Exibindo o salário anual de cada funcionário
    print(f"Salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

    # Aplicando um aumento de 10% para cada funcionário
    emp1.dar_aumento(10)
    emp2.dar_aumento(10)

    # Exibindo os salários anuais após o aumento
    print(f"Novo salário anual de {emp1.nome} {emp1.sobrenome} ({emp1.departamento}): R${emp1.salario_anual():.2f}")
    print(f"Novo salário anual de {emp2.nome} {emp2.sobrenome} ({emp2.departamento}): R${emp2.salario_anual():.2f}")

if __name__ == "__main__":
    main()
