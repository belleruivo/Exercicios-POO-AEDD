'''
7. Faça um programa que cadastre n alunos. Para cada aluno devem ser cadastrados
nome e nota final. Os dados devem ser armazenados em uma lista duplamente
encadeada e não ordenada. Em seguida, o programa deve mostrar apenas o nome
dos alunos aprovados, ou seja, alunos com nota final de no mínimo 7. Se nenhum
aluno estiver aprovado, mostrar mensagem.
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None