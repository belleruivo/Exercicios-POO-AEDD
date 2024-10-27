class ComparableStudent:
    def compare(self, other):
        if self == other:
            return "Os nomes são iguais."
        elif self < other:
            return f"{self.name} vem antes de {other.name}."
        elif self >= other:
            return f"{self.name} vem depois ou é igual a {other.name}."
