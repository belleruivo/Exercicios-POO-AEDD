class Card:
    def __init__(self, naipe: str, valor: str):
        self.naipe = naipe #string
        self.valor = valor

    def __str__(self) -> str:
        return f"{self.valor} de {self.naipe}"
