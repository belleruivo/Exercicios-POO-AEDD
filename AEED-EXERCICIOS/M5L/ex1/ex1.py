"""1. Escreva um programa que use uma pilha para testar strings de entrada e determinar
se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma
forma de frente para trás e de trás para a frente; por exemplo, arara."""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        return None if self.is_empty() else self.top.value


def is_palindrome(s):
    stack = Stack()
    cleaned_string = ''.join(caractere.lower() for caractere in s if caractere.isalnum())  

    for caractere in cleaned_string:
        stack.push(caractere)

    for caractere in cleaned_string:
        if caractere != stack.pop():
            return False

    return True

user_input = input("Digite uma string para verificar se é um palíndromo: ")
if is_palindrome(user_input):
    print(f'"{user_input}" é um palíndromo.')
else:
    print(f'"{user_input}" não é um palíndromo.')