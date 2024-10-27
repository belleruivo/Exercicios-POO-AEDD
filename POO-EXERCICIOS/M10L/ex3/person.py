class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int):
        self._age = age

    def __str__(self):
        return f'Name: {self._name}, Age: {self._age}'
