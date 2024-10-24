from abc import ABC, abstractmethod
from Library import Library

class LibraryAction(ABC):
    """Classe base para todas as ações da biblioteca."""
    
    def __init__(self, library: Library):
        # Inicializa a ação da biblioteca com uma instância da biblioteca
        self.library = library

    @abstractmethod
    def execute(self):
        """Executa a ação."""
        # Método abstrato que deve ser implementado pelas subclasses
        pass
    
# o pass Palavra-chave que indica que o método não faz nada por enquanto, mas deve ser implementado nas subclasses.
