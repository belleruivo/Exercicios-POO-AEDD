"""1. Escreva um programa que use uma pilha para testar strings de entrada e determinar
se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma
forma de frente para trás e de trás para a frente; por exemplo, arara."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        return False

    def push(self, new_data):
        new_node = Node(new_data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Empty stack")
            return None
        else:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data

    def peek(self):
        return None if self.is_empty() else self.head.data
    


def is_palindrome(word):
    stack = Stack()
    cleaned_string = ''.join(caractere.lower() for caractere in word if caractere.isalpha()) #mantém apenas letra e números

    if not cleaned_string:
        return False
    
    for c in cleaned_string:
        stack.push(c)

    for c in cleaned_string:
        if c != stack.pop():
            return False

    return True

def main():
    word = input("Digite uma string para verificar se é um palíndromo: ")
    if is_palindrome(word):
        print(f'"{word}" é um palíndromo.')
    else:
        print(f'"{word}" não é um palíndromo.')

main()