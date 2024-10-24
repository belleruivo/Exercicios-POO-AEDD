from GuessingGame import GuessingGame

class ExtendedGuessingGame(GuessingGame):
    def __init__(self):
        # Chama o construtor da classe base GuessingGame
        super().__init__()
        # Inicializa o contador de tentativas
        self.attempts = 0

    def guess(self, player_guess):
        # Incrementa o contador de tentativas a cada palpite
        self.attempts += 1
        
        # Chama o método guess da classe base e armazena o resultado
        result = super().guess(player_guess)
        
        # Verifica se o palpite foi correto
        if result == "Parabéns! Você adivinhou o número.":
            # Adiciona o número de tentativas ao resultado
            result += f" Você levou {self.attempts} tentativas."
        
        # Retorna o resultado
        return result