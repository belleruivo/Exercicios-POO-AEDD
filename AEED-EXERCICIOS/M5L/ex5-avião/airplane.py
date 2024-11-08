class Airplane:
    def __init__(self, name, id_number, model, manufacturer):
        self.name = name           # Nome do avião.
        self.id_number = id_number # ID do avião (número inteiro).
        self.model = model         # Modelo do avião.
        self.manufacturer = manufacturer  # Fabricante do avião.

    def __str__(self):
        return f"Avião: {self.name}, ID: {self.id_number}, Modelo: {self.model}, Fabricante: {self.manufacturer}"
