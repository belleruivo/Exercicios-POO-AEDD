from student import Student
from papel_lider import PapelLider
from participacao_clube import ParticipacaoClube
from perfil_academico import PerfilAcademico

class Graduacao(Student):
    
    def __init__(self, nome, idade, curso, clube):
        perfil = PerfilAcademico("Graduação")
        super().__init__(nome, idade, curso, perfil)
        self.papel_lider = PapelLider()
        self.participacao_clube = ParticipacaoClube(clube)

    def obter_papeis(self):
        return {
            "lider": self.papel_lider.is_lider(),
            "clube": self.participacao_clube.get_clube()
        }
