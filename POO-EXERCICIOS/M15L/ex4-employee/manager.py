from employee import Employee
from itrainable import ITrainable
from idepartment_assignable import IDepartmentAssignable
from isalary_adjustable import ISalaryAdjustable

class Manager(Employee, ITrainable, IDepartmentAssignable, ISalaryAdjustable):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_job_description(self):
        return f"Gerente do departamento {self.department}."

    def conduct_training(self):
        return f"{self.name} está conduzindo um treinamento no departamento {self.department}."

    def assign_department(self, department: str):
        self.department = department
        return f"{self.name} agora é gerente do departamento {self.department}."

    def adjust_salary(self, percentage: float):
        self.salary += self.salary * (percentage / 100)
        return f"Novo salário de {self.name}: {self.salary}"

    def __str__(self):
        return f"{super().__str__()} (Gerente - {self.department})"


# Registro como subclasse virtual
ITrainable.register(Manager)
IDepartmentAssignable.register(Manager)

# O método register() foi usado para registrar as classes como subclasses virtuais das interfaces. Isso é importante porque o Python permite que uma classe seja registrada como uma subclasse de uma interface abstrata sem ser obrigada a implementar todos os métodos da interface imediatamente.

# Isso registra a classe Manager como uma "subclasse virtual" da interface ITrainable e IDepartmentAssignable. Isso significa que, embora a classe Manager implemente esses métodos (como conduct_training e assign_department), ela não é obrigada a herdar diretamente de cada uma dessas interfaces. O register() permite que a classe seja reconhecida como compatível com as interfaces sem realmente ter que fazer uma herança formal.

# Por que usar o register()?

# Ele minimiza a necessidade de herança múltipla: você não precisa que a classe Manager herde diretamente de várias interfaces, o que evita a complicação de heranças complexas. Ao invés disso, você usa o register() para "conectar" a classe com a interface sem herança direta.
# Permite maior flexibilidade no design das classes e das interfaces.
# O Que Foi Implementado
# Interfaces específicas (ITrainable e IDepartmentAssignable) foram criadas e aplicadas nas classes Manager e Salesperson, para que essas classes implementem apenas os métodos que realmente precisam.
# Subclasses virtuais: o método register() foi utilizado para registrar as classes como implementadoras das interfaces sem a necessidade de herança direta.
# Resumo da Implementação
# Segregação de Interface:

# Duas interfaces específicas (ITrainable e IDepartmentAssignable) foram criadas para funções específicas.
# O Manager implementa as duas interfaces, enquanto Salesperson implementa apenas a interface relacionada ao departamento.
# Uso do register():

# O register() foi utilizado para fazer o "registro" de classes como subclasses virtuais das interfaces, evitando a herança múltipla e mantendo a flexibilidade do design.
