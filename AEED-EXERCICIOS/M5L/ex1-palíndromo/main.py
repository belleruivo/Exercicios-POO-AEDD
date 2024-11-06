"""1. Escreva um programa que use uma pilha para testar strings de entrada e determinar
se são palíndromos. Um palíndromo é uma sequência de caracteres lida da mesma
forma de frente para trás e de trás para a frente; por exemplo, arara."""

from stack import Stack

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