# Classe base Animal
class Animal:
    def _init_(self, nome: str, raca: str):
        self.nome = nome
        self.raca = raca

    def andar(self) -> str:
        return f"{self.nome} está andando."

# Classe Dog (Cachorro) herda de Animal
class Dog(Animal):
    def _init_(self, nome: str, raca: str):
        super()._init_(nome, raca)

    def latir(self) -> str:
        return f"{self.nome} diz: Au au!"

# Classe Cat (Gato) herda de Animal
class Cat(Animal):
    def _init_(self, nome: str, raca: str):
        super()._init_(nome, raca)

    def miar(self) -> str:
        return f"{self.nome}diz: Miau!"