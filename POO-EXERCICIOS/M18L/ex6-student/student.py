from abc import ABC, abstractmethod
from curso import Curso
from historico import Historico
from endereco import Endereco

class Student(ABC):
    
    def __init__(self, nome, idade, curso, endereco, historico=None):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.endereco = endereco
        self.historico = historico if historico else Historico()
    
    @abstractmethod
    def get_student_type(self):
        pass

    def get_curso(self):
        return self.curso.get_nome()

    def get_endereco(self):
        return self.endereco.get_endereco_completo()

    def get_historico(self):
        return self.historico.calcular_media()
