'''
6. Dada uma lista encadeada de caracteres formada por uma sequência alternada de
letras e dígitos, construa um método que retorne uma lista na qual as letras são
mantidas na sequência original e os dígitos são colocados na ordem inversa.
Exemplos:

3
A 1 E 5 T 7 W 8 G → A E T W G 8 7 5 1
3 C 9 H 4 Q 6 → C H Q 6 4 9 3
Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos
dígitos. Sugestões: usar uma fila e uma pilha; e supor um método ehDigito() retorna
booleano que retorna verdadeiro caso um caractere seja um dígito.
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # o próximo nó
