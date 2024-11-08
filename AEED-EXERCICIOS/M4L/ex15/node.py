'''
15. Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que copie
o conteúdo de um vetor para uma lista encadeada preservando a ordem dos
elementos e outra função que copie o conteúdo de uma lista encadeada para um
vetor preservando a ordem dos elementos. Faça duas versões: uma iterativa e uma
recursiva.
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None