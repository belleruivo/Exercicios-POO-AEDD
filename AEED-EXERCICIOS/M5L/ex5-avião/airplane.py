class Airplane:
    def __init__(self, name, id_number, model, manufacturer):
        self.name = name
        self.id_number = id_number
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return f"Avião: {self.name}, ID: {self.id_number}, Modelo: {self.model}, Fabricante: {self.manufacturer}"