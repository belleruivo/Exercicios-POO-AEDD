# aluno.py
class Aluno:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.notas = []

class PilhaAlunos:
    def __init__(self):
        self.alunos = []
        self.proximo_numero = 1

    def cadastrar_aluno(self, nome):
        if not nome.strip():
            return "Nome inválido. Por favor, insira um nome válido."
        aluno = Aluno(self.proximo_numero, nome.strip())
        self.alunos.append(aluno)
        self.proximo_numero += 1
        return "Aluno cadastrado."

    def obter_aluno(self, numero):
        try:
            numero = int(numero)
            for aluno in self.alunos:
                if aluno.numero == numero:
                    return aluno
            return None
        except ValueError:
            return None

    def excluir_aluno(self):
        if not self.alunos:
            return "Pilha vazia."
        aluno = self.alunos[-1]
        if aluno.notas:
            return "Este aluno possui notas, logo, não poderá ser excluído."
        self.alunos.pop()
        return "Aluno excluído."

    def listar_alunos_sem_nota(self):
        sem_notas = [aluno.nome for aluno in self.alunos if not aluno.notas]
        if not sem_notas:
            return "Todos os alunos possuem notas."
        return "\n".join(sem_notas)
