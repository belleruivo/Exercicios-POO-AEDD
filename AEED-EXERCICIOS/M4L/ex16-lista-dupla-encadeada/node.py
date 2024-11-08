class Node:
    """Classe que representa um nó da lista encadeada."""
    
    def __init__(self, data, next=None, previous=None):
        """Inicializa um nó com dados e ponteiros para o próximo e o anterior."""
        self.data = data
        self.next = next
        self.previous = previous
