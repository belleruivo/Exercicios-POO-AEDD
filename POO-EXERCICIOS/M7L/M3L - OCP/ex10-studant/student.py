from comparables import ComparableStudent

class Student(ComparableStudent):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # Validação da nota
        if not (1 <= grade <= 10):
            raise ValueError("A nota deve estar entre 1 e 10.")

    # Método para testar igualdade de nomes
    def __eq__(self, other):
        return self.name == other.name

    # Método para testar se um nome é menor que o outro
    def __lt__(self, other):
        return self.name < other.name

    # Método para testar se um nome é maior ou igual ao outro
    def __ge__(self, other):
        return self.name >= other.name

    # Método para exibir as informações do estudante
    def print_info(self):
        print(f"Nome: {self.name}, Nota: {self.grade}")

    # Método de comparação (implementação do método da classe base)
    def compare(self, other):
        # Utiliza o método de comparação da classe base
        return super().compare(other)
