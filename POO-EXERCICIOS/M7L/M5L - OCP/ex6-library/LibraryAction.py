from abc import ABC, abstractmethod
from Library import Library

class LibraryAction(ABC):
    """Classe base para todas as ações da biblioteca."""
    def __init__(self, library: Library):
        self.library = library

    @abstractmethod
    def execute(self):
        """Executa a ação."""
        pass
