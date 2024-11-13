class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def animal(self, name=None):
        pass
    
    def walk(self):
        pass
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)