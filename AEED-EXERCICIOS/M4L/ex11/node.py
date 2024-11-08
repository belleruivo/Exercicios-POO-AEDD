'''
11. Faça um programa que implemente uma lista encadeada de números inteiros com
inserção de dados pelo usuário através de um menu. Escreva uma função que
encontre o nó que contenha o menor valor e outra função que verifique se duas listas
encadeadas são iguais, ou melhor, se têm o mesmo conteúdo. Faça duas versões:
uma iterativa e uma recursiva.
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None