# nota.py
from aluno import PilhaAlunos

class Nota:
    def __init__(self, numero_aluno, valor):
        self.numero_aluno = numero_aluno
        self.valor = valor

class FilaNotas:
    def __init__(self):
        self.notas = []

    def cadastrar_nota(self, numero_aluno, valor, pilha_alunos):
        try:
            numero_aluno = int(numero_aluno)
            valor = float(valor)
        except ValueError:
            return "Dados inválidos. Insira um número de aluno e uma nota válidos."

        aluno = pilha_alunos.obter_aluno(numero_aluno)
        if aluno is None:
            return "Aluno não cadastrado."
        nota = Nota(numero_aluno, valor)
        aluno.notas.append(valor)
        self.notas.append(nota)
        return "Nota cadastrada."

    def excluir_nota(self):
        if not self.notas:
            return "Fila vazia."
        self.notas.pop(0)
        return "Nota excluída."
