class Dificuldade:
    def __init__(self, nivel):
        self.nivel = nivel
        self.intervalo = self.definir_intervalo()

    def definir_intervalo(self):
        """Define o intervalo de números com base no nível de dificuldade."""
        if self.nivel == 'fácil':
            return (1, 50)
        elif self.nivel == 'médio':
            return (1, 100)
        elif self.nivel == 'difícil':
            return (1, 200)
        else:
            raise ValueError("Nível de dificuldade inválido.")
