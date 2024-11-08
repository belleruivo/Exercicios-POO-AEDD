'''
3. Defina uma função chamada pop que remove o item em determinada posição de uma
estrutura unicamente ligada. Essa função espera uma posição como primeiro
argumento, com a precondição 0 <= posição < comprimento da estrutura. Seu
segundo argumento é a estrutura ligada, que, é claro, não pode estar vazia. A função
retorna uma tupla contendo a estrutura ligada modificada e o item que foi removido.
Um exemplo de chamada é (head, item) = pop(1, head).
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next  # o próximo nó