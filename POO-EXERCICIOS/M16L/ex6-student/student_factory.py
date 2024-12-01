from graduacao import Graduacao
from especializacao import Especializacao
from mestrado import Mestrado
from doutorado import Doutorado

class StudentFactory:
    
    @staticmethod
    def create_student(tipo, nome, idade, clube=None):
        if tipo == 1:
            return Graduacao(nome, idade, clube)
        elif tipo == 2:
            return Especializacao(nome, idade)
        elif tipo == 3:
            return Mestrado(nome, idade)
        elif tipo == 4:
            return Doutorado(nome, idade)
        else:
            raise ValueError("Tipo inválido.")
