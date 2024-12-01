from graduacao import Graduacao
from especializacao import Especializacao
from mestrado import Mestrado
from doutorado import Doutorado
from curso import Curso

class StudentFactory:
    
    @staticmethod
    def create_student(tipo, nome, idade, curso_nome, clube=None):
        curso = Curso(curso_nome)
        if tipo == 1:
            return Graduacao(nome, idade, curso, clube)
        elif tipo == 2:
            return Especializacao(nome, idade, curso)
        elif tipo == 3:
            return Mestrado(nome, idade, curso)
        elif tipo == 4:
            return Doutorado(nome, idade, curso)
        else:
            raise ValueError("Tipo inválido.")
